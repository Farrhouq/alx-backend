import redis from 'redis';

const redisCli = redis.createClient();

redisCli.on('error', (error) => {
  console.log(`Redis client not connected to the server: ${error}`);
});

redisCli.on('connect', () => {
  console.log('Redis client connected to the server');
});

const data = {
  Portland: 50,
  Seattle: 80,
  'New York': 20,
  Bogota: 20,
  Cali: 40,
  Paris: 2,
};

for (const k in data) {
  redisCli.HSET('HolbertonSchools', k, data[k], redis.print);
}

redisCli.HGETALL('HolbertonSchools', (error, reply) => {
  if (error) {
    throw (error);
  } else {
    console.log(reply);
  }
});
