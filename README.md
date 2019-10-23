# Crowler
Crawler for StudCee resources file system which generates briefings on inventories for various courses.

### Usage
```
usage: crowler.py [-h] [--block BLOCK] [--year YEAR] [--programme PROGRAMME]

optional arguments:
  -h, --help            show this help message and exit
  --block BLOCK         the block number of interest
  --year YEAR           the year number of interest
  --programme PROGRAMME the degree of interest
```
### Example
```
python3 crowler.py --programme "BSc AI" --year 0 --block 0

*StudCee Resources Available for Your Course!*

Imperative Programming
- 15 Exams
- 1 Summaries
- 3 Useful Links

Autonomous Systems
- 2 Summaries

Introduction to Artificial Intelligence
- 1 Summaries

*Access all these and more at: studcee.svcover.nl*
```
