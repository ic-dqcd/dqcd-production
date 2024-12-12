# dqcd-production

## Production
This repository uses central production to generate the necessary samples. See

https://gitlab.cern.ch/cms-exo-mci/EXO-MCsampleRequests
https://exo-mc-and-i.gitbook.io/exo-mc-and-interpretation/how-to-sample-request#instructions

For it to work, we need EXO-MCsampleRequests to work with
- CMSSW_14_0_18
- --conditions 124X_mcRun3_2022_realistic_v12

## Installation

Clone the repository with
```
git clone git@github.com:ic-dqcd/dqcd-production.git -b 2024
````

Make a fork of EXO-MCsampleRequests and clone it to lxplus
(follow instructions as in https://exo-mc-and-i.gitbook.io/exo-mc-and-interpretation/how-to-sample-request)

Move the configuration files and request.csv to the corrrect directory in EXO-MCsampleRequests
```
cp dqcd-production/python/request.csv EXO-MCsampleRequests/
cp -r dqcd-production/python/ EXO-MCsampleRequests/genFragments/dqcd
```

Follow the tests as described in https://exo-mc-and-i.gitbook.io/exo-mc-and-interpretation/how-to-sample-request
