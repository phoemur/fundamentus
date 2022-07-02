# Deploy Fundamentus

    oc new-project fundamentus

    oc new-app --name fundamentus --labels app=fundamentus https://github.com/laurobmb/fundamentus.git#master --context-dir app --strategy=docker

    oc new-app --name fundamentus --labels app=fundamentus https://github.com/laurobmb/fundamentus.git#master --context-dir app --strategy=source --env ENVIROMENT="prod"

    oc expose svc fundamentus

    oc -n fundamentus expose service fundamentus

    oc -n fundamentus expose service fundamentus --name fundamentus-hml --hostname fundamentus-fundamentus.hml.lagomes.rhbr-lab.com

    oc -n fundamentus create route edge fundamentus-tls --service fundamentus

    oc -n fundamentus set probe deployment/fundamentus --readiness --initial-delay-seconds=10 --timeout-seconds=30 --get-url=http://:8080/health

    oc -n fundamentus set probe deployment/fundamentus --liveness --initial-delay-seconds=10 --timeout-seconds=30 --get-url=http://:8080/health

    oc -n fundamentus set resources deployment/fundamentus --limits=cpu=250m,memory=256Mi --requests=cpu=100m,memory=64Mi

    oc -n fundamentus autoscale deployment fundamentus --max 10 --min 2 --cpu-percent=80

    oc -n fundamentus create quota fundamentus-quota --hard=cpu=500m,memory=500Mi
