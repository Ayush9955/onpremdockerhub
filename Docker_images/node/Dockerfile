FROM node:alpine
    
    WORKDIR /app
    
    COPY . /app
    
    RUN if [ "$PACKAGE_MANAGER" = "yarn" ]; then yarn; else npm install; fi
    
    EXPOSE 3000
    
    CMD if [ "$PACKAGE_MANAGER" = "yarn" ]; then yarn start; else npm start; fi
    