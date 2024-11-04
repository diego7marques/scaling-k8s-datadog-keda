import http from 'k6/http';
import { sleep } from 'k6';

// Read the API path from an environment variable
const API_PATH = __ENV.API_PATH;
const BASE_URL = '<BASE_ENDPOINT>';

const API_URL = BASE_URL + API_PATH;

// Define the options for the load test
export let options = {
    duration: '2m',
    vus: 10, // Number of Virtual Users
    iterations: 300, // Total number of requests
};

export default function () {
    // Send a GET request to the API
    http.get(API_URL);

    // Optional: Add a sleep (3s) to simulate real-world usage
    sleep(3);
}