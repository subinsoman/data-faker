# data-faker
[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

## Getting Started

just config schema to genrate file


```
length: 1000000
columns:
  - name: 'I_MSISDN'
    type: int64
    params:
      min: 9999999990
      max: 9999999999
  - name: 'I_RECHARGE_AMOUNT'
    type: int64
    params:
      min: 120
      max: 150
  - name: 'SEQUNCE'
    type: int64
    params:
      min: 0
      max: 10
```
run via 

```
python generator.py examples/financial.yaml -o /root/dummydata/result2.csv
```

build as a debian app

cd data_faker   (the folder contains setup.py)
```
pip install .
```
then 
```
datafaker examples/financial.yaml -o /root/dummydata/result2.csv
```

## Authors

* **subin soman** - *Initial work* - [subinsoman](https://github.com/subinsoman)


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
SUBIN x
