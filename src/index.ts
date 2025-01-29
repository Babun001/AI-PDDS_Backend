import  dotenv from 'dotenv';
dotenv.config({
    path:'./.env'
});

import app from './app.js';

try {
    app.listen(process.env.PORT, () =>{
        console.log(`Server is running on http://localhost:${process.env.PORT}`);
        
    })
} catch (error) {
    console.error("Server failed "+ error);
    process.exit(1);
}
