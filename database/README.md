# database

```
export DB_PW=$(kubectl get secret --namespace hermes postgres-postgresql -o jsonpath="{.data.postgresql-password}" | base64 --decode)
```
