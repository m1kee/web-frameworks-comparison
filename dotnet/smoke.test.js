import http from 'k6/http';
import { check, sleep } from 'k6';

export const options = {
  vus: 1, // 1 user looping for 1 minute
  duration: '1m',

  thresholds: {
    http_req_duration: ['p(99)<500'], // 99% of requests must complete below .5s
  },
};

let url = 'http://localhost:5128/';

export default () => {
  const resp = http.get(url);

  check(resp, {
    'received data successfully': (resp) => resp.json('message') !== '',
  });

  sleep(1);
};