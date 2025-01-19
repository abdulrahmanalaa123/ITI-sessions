FROM nginx:latest
RUN rm /etc/nginx/conf.d/default.conf
EXPOSE 4000
COPY nginx.conf /etc/nginx/
COPY index.html /usr/share/nginx/html