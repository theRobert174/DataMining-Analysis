
# Data Mining - Analysis Who Suicide?

* Rodrigo Antonio Martinez Macias
* 1896222

## Who suicide statistics

| Dato           | Descripcion                                                |
|----------------|------------------------------------------------------------|
| country        | pais donde sucedieron los hechos                           |
| year           | año el cual se registraron los sucesos                     |
| sex            | persona hombre o mujer                                     |
| age            | rango de edades de las personas                            |
| suicides_no    | cantidad de gente que cometió el acto                      |
| population     | total de poblacion por rango de edades en cada año         |

## Diagrama de objetos
```mermaid
classDiagram
    class Country {
        - id: Int
        - Name: String
    }

    class Year {
        - id: Int
        - Date: DateTime        
    }

    class sex {
        - id: Int
        - sex: String        
    }

    class rangeAge {
        - id: Int
        - range: String        
    }

    class Data {
        - id: Int
        - suicides: Integer
        - population: Long
    }

    Country "1:M" -- "1:M" Year
    Year "1:M" -- "1:M" sex
    sex "1:M" -- "1:M" rangeAge
    rangeAge "1:1" -- "1:1" Data
```


## Authors

- [@theRobert174](https://www.github.com/theRobert174)


## 🚀 About Me
I'm a full stack developer... in development :)

