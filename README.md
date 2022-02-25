
Implementation of real-world application: https://github.com/gothinkster/realworld/ using Django and HTMX.

An in-depth discussion of this implementation can be found [here](https://danjacob.net/posts/anatomyofdjangohtmxproject/).

Tech Stack:

* [InterSystems IRIS](https://www.intersystems.com/products/intersystems-iris/)
* [Django](https://djangoproject.com)
* [HTMX](https://htmx.org)
* [Alpine](https://alpinejs.dev)

To install and run with docker-compose (requires iris.key placed in the home directory):

```bash
git clone https://github.com/caretdev/django-iris-realworld/ && cd realworld

docker-compose up -d --build
```


**Note: this is just a reference implementation and is not intended for production use.**
