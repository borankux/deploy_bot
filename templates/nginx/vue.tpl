server {
        listen       80;
        server_name  {{SERVER_NAME}};
        root         {{ROOT}};
        index index.html;
        #charset koi8-r;

        gzip on;
        gzip_min_length 1k;
        gzip_buffers 4 16k;
       #gzip_http_version 1.0;
        gzip_comp_level 2;
        gzip_types text/plain application/x-javascript text/css application/xml text/javascript application/x-httpd-php image/jpeg image/gif image/png;
        gzip_vary off;
        gzip_disable "MSIE [1-6]\.";

        access_log  {{ACCESS_LOG}}  main;

        location /{
            try_files $uri $uri/ @router;
            index index.html index.htm;
        }

        location @router {
            rewrite ^.*$ /index.html last;
        }
}