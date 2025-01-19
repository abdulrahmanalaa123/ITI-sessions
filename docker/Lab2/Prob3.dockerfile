FROM node:latest AS building
RUN npm install -g vite
RUN npm create vite@latest react-app -- --template react
WORKDIR /react-app
RUN npm install
COPY vite.config.js .
RUN npm run build
#EXPOSE 5173 
#CMD ["npm","run","dev","--","--host"]

FROM nginx:1.27.3-alpine
COPY --from=building react-app/dist/ /usr/share/nginx/html
EXPOSE 80

#FROM node:22-slim
#RUN npm i -g serve
#COPY --from=building /react-app/dist /serve
#EXPOSE 8080
#CMD ["serve","-s","-p","8080","serve"]
