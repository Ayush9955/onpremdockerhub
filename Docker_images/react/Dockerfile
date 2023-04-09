    FROM node:alpine
    
    WORKDIR /oortfy
    
    COPY . /oortfy
    
    RUN if [ "$PACKAGE_MANAGER" = "yarn" ]; then yarn; else npm install; fi
    
    RUN npm install react-scripts@${react_base_version} -g --silent
    
    EXPOSE 3000
    
    CMD if [ "$PACKAGE_MANAGER" = "yarn" ]; then yarn start; else npm start; fi
    