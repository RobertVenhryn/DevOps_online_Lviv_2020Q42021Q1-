I've done my home task in this way: my index.html file was changed and pushed to GitHub by a developer on my ubuntu instance, after that Jenkins has started the job "Deploy_to_prod_fromGitHub(auto)_with_slaves" (means master sent this job to the slave - another Ubuntu instance on AWS). After that, this slave took the code from the repository on GitHub and made changes to the index.html file in the end. After sending the file to GitHub (git push) everything proceeds automatically.

![Screenshot_1](https://user-images.githubusercontent.com/75696130/108414425-e1f92700-7234-11eb-8de3-2756e48daa22.png)

![Screenshot_2](https://user-images.githubusercontent.com/75696130/108414438-e4f41780-7234-11eb-972e-08f263bc91ff.png)

![Screenshot_3](https://user-images.githubusercontent.com/75696130/108414448-e8879e80-7234-11eb-8d98-dfb99f9fca46.png)

![Screenshot_4](https://user-images.githubusercontent.com/75696130/108414456-eb828f00-7234-11eb-9d93-4ccdb43e313c.png)

![Screenshot_5](https://user-images.githubusercontent.com/75696130/108414462-ef161600-7234-11eb-92cf-487dcd832506.png)

![Screenshot_6](https://user-images.githubusercontent.com/75696130/108414473-f1787000-7234-11eb-8549-417b131196ec.png)

![Screenshot_7](https://user-images.githubusercontent.com/75696130/108414479-f4736080-7234-11eb-8c8c-0a52202f85ac.png)

![Screenshot_8](https://user-images.githubusercontent.com/75696130/108414488-f6d5ba80-7234-11eb-9823-d9bc23adb50d.png)
