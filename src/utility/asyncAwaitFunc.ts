import { Request, Response, NextFunction } from "express"
const asyncAwaitFunc = (requestFunc:(req:Request, res:Response , next:NextFunction) => Promise<any> | void) =>{
    return (req:Request, res:Response , next:NextFunction) =>{
        Promise.resolve(requestFunc(req, res , next)).catch(err => next(err))
    }
}

export default asyncAwaitFunc;