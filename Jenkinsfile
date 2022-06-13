node {
    stage('Build') {
        echo 'Building....'
        checkout scm
        sh "docker login -u admin -p Ccwtn@123 192.168.44.129:8081"
        sh "docker build . -t django-web-backend"
        sh "docker tag django-web-backend:latest 192.168.44.129:8081/sse/django-web-backend:2.0"
        sh "docker push 192.168.44.129:8081/sse/django-web-backend:2.0"
    }
    stage('Test') {
        echo 'Building....'
    }
    stage('Deploy') {
        echo 'Deploying....'
    }
}
