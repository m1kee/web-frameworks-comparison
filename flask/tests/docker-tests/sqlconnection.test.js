import http from 'k6/http';
import { sleep } from 'k6';

let url = 'http://10.101.78.145:4001/users';

export const options = {
  stages: [
    { duration: '2m', target: 20 },
    { duration: '8m', target: 20 },
  ],
};

export default function () {
  const responses = http.batch([
    ['GET', url, null],
  ]);

  sleep(1);
}