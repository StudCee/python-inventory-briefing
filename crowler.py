import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--block', type=int,
                   help='the block number of interest', default=0)

parser.add_argument('--year', type=int,
                   help='the year number of interest', default=0)

parser.add_argument('--programme', type=str,
                   help='the degree of interest', default='BSc AI')

args = parser.parse_args()

programmes = {
    'BSc AI': {
        'level': 'bachelor',
        'courses': [
            [
                'Imperative Programming',
                'Autonomous Systems',
                'Introduction to Artificial Intelligence'
            ]
        ]
    }
}

print('\n*StudCee Resources Available for Your Course!*\n')

if programmes[args.programme]['level'] == 'bachelor':
    prefix = 'data/2 Bachelor Courses/'
else:
    prefix = 'data/3 Master Courses/'


for course in programmes[args.programme]['courses'][args.year * 4 + args.block]:
    print(course)

    exam_address = prefix + course + '/Exams'
    summaries_address = prefix + course + '/Summaries'
    external_address = prefix + course + '/External Lectures'
    links_address = prefix + course + '/Useful links'

    if os.path.exists(exam_address):
        exam_count = len(os.listdir(exam_address))

        if exam_count > 0:
            print('-', exam_count, 'Exams & Solutions')

    if os.path.exists(summaries_address):      
        summaries_count = len(os.listdir(summaries_address))

        if summaries_count > 0:
            print('-', summaries_count, 'Summaries')
    
    if os.path.exists(external_address):
        external_address = len(os.listdir(external_address))

        if external_address > 0:
            print('-', external_address, 'External Lectures')
    
    if os.path.exists(links_address):
        links_address = len(os.listdir(links_address))

        if links_address > 0:
            print('-', links_address, 'Useful Links')

    print()

print('*Access all these and more at: studcee.svcover.nl*\n')
