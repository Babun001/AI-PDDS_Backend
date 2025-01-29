import express from 'express';
import cors from 'cors';
import cookieParser from 'cookie-parser';

const app = express();

app.use(cors({
    origin: process.env.CORS_PORT
}))

app.use(express.json());

// app.use(cookieParser());

app.use(express.static("public"))

app.use(express.urlencoded({ extended: true }));

import apiRoute from './routes/disease.routes';

app.use('/diabetes/api/v1',apiRoute);
// app.use('/')

export default app;

