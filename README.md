# Registro de séries
 Sistema para armazenamento e criação de séries, usando Flask, PostgreSQL e Psycopg2.
 

## Rotas

> POST /series

- Body da requisição.
```json
{
    "serie": "Serie name",
    "seasons": 2,
    "released_date": "11/10/2016",
    "genre": "Drama",
    "imdb_rating": 4.5
}
```
- Retorno da requisição.
```json
{
  "genre": "Drama",
  "id": 1,
  "imdb_rating": 4.5,
  "released_date": "Tue, 11 Oct 2016 00:00:00 GMT",
  "seasons": 2,
  "serie": "Serie Name"
}
```

>GET /series
- Caso o banco esteja vazio.

```json
{
  "Data": []
}
```

>GET /series
- Caso tenha dados cadastrados.

```json
{
  "data": [
    {
      "genre": "Drama",
      "id": 1,
      "imdb_rating": 4.5,
      "released_date": "Tue, 11 Oct 2016 00:00:00 GMT",
      "seasons": 2,
      "serie": "Serie Name"
    },
    {
      "genre": "Comedia",
      "id": 2,
      "imdb_rating": 7.8,
      "released_date": "Tue, 11 Oct 2016 00:00:00 GMT",
      "seasons": 4,
      "serie": "Serie Name"
    }
  ]
}
```

>GET /series/<serie_id>
- Passar como paramêtro o ID da serie para consulta específica.

```python
#Ex: /serie/1

{
  "data": {
    "genre": "Drama",
    "id": 1,
    "imdb_rating": 4.5,
    "released_date": "Tue, 11 Oct 2016 00:00:00 GMT",
    "seasons": 2,
    "serie": "Serie Name"
  }
}
```