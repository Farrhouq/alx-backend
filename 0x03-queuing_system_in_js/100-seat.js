import redis from 'redis';
import kue from 'kue';
import express from 'express';
import { promisify } from 'util';

const redisCli = redis.createClient();
const queue = kue.createQueue();
const app = express();

const asyncSet = promisify(redisCli.set).bind(redisCli);
const asyncGet = promisify(redisCli.get).bind(redisCli);

async function reserveSeat(number) {
  await asyncSet('available_seats', number);
}

reserveSeat(50);

async function getCurrentAvailableSeats() {
  const s = await asyncGet('available_seats');
  return parseInt(s) || 0;
}

let reservationEnabled = true;

app.listen(1245, () => {
  console.log('Server running on port 1245');
});

app.get('/available_seats', async (req, res) => {
  const numberOfAvailableSeats = await getCurrentAvailableSeats();
  res.json({ numberOfAvailableSeats });
});

app.get('/reserve_seat', async (req, res) => {
  if (!reservationEnabled) {
    res.json({ status: 'Reservation are blocked' });
    return;
  }
  const job = queue.create('reserve_seat', {});

  job.on('enqueue', () => {
    console.log('Reservation in progress');
  });
  job.on('complete', () => {
    console.log(`Seat reservation job ${job.id} completed`);
  });
  job.on('failed', (error) => {
    console.log(`Seat reservation job ${job.id} failed: ${error.message || error.toString()}`);
  });
  job.save();
  res.json({ status: 'Reservation in progress' });
});

app.get('/process', async (req, res) => {
  console.log('Queue processing');
  queue.process('reserve_seat', async (job, done) => {
    const curAvailSeats = await getCurrentAvailableSeats();
    if (curAvailSeats === 0) {
      reservationEnabled = false;
      done(new Error('Not enough seats available'));
    } else {
      await reserveSeat(curAvailSeats - 1);
      if (curAvailSeats - 1 === 0) {
        reservationEnabled = false;
      }
      done();
    }
  });
  res.json({ status: 'Queue processing' });
});
