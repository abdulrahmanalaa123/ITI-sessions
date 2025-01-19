FROM node:latest
RUN npm install -g vite
RUN npm create vite@latest react-app -- --template react
WORKDIR /react-app
RUN npm install
COPY vite.config.js .
EXPOSE 5173
CMD ["npm","run","dev","--","--host"]
