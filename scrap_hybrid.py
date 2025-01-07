import json
import traceback

from bs4 import BeautifulSoup

url_base = 'https://www.hybridcalisthenics.com'

if False:
    fetch(url_base + '/index')

    mvt_urls = {}
    for mvt in response.css('p'):
        mvt_n = mvt.css('strong::text').get()
        if mvt_n is None:
            continue
        mvt_urls[mvt_n] = mvt.css('a::attr(href)').getall()

mvt_urls = {
    'Pushups': ['/pushups', '/wall-pushups', '/incline-pushups', '/advanced-incline-pushups', '/knee-pushups', '/full-pushups', '/narrow-pushups', '/side-staggered-pushups', '/archer-pushups', '/sliding-onearm-pushups', '/onearm-pushups', '/advanced-onearm-pushups'],
    'Leg Raises': ['/legraises', '/knee-raises', '/advanced-knee-raises', '/alternating-leg-raises', '/full-leg-raises', '/tuck-plow-raises', '/plow-raises', '/hanging-knee-raises', '/hanging-leg-raises', '/toe-to-bars'],
    'Pullups': ['/pullups', '/wall-pullups', '/horizontal-pullups', '/advanced-horizontal-pullups', '/jackknife-pullups', '/full-pullups', '/narrow-pullups', '/one-hand-pullups', '/advanced-onehand-pullups', '/archer-pullups', '/one-arm-pullups'],
    'Squats': ['/squats', '/jackknife-squats', '/assisted-squats', '/half-squats', '/full-squats', '/narrow-squats', '/side-staggered-squats', '/front-staggered-squats', '/assisted-oneleg-squats', '/one-leg-chair-squats', '/oneleg-squats'],
    'Twists': ['/twists', '/straight-leg-twists', '/bent-leg-twists', '/full-twists'],
    'Bridges': ['/bridges', '/glute-bridges', '/straight-bridges', '/wall-bridges', '/incline-bridges', '/head-bridges', '/full-bridges', '/wheel-bridges', '/tap-bridges', '/wallwalking-bridges', '/standtostand-bridges'],
    'Dips': ['/dips', '/bent-knee-bench-dips', '/bench-dips', '/elevated-bench-dips', '/jackknife-parallel-dips', '/assisted-parallel-dips', '/parallel-dips'],
    'Clutch Flags': ['/clutchflags', '/clutch-flag-grip', '/single-leg-diagonal-flag', '/bent-knee-diagonal-flag', '/full-diagonal-flag', '/tuck-clutch-flag', '/single-leg-clutch-flag', '/bent-knee-clutch-flag', '/clutch-flag'],
    'Lunges': ['/lunges', '/wall-press-lunges', '/assisted-leg-press-lunges', '/leg-press-lunges', '/bodyweightlunges', '/assisted-deep-lunges', '/deep-lunges'],
    'Elbow Levers': ['/elbowlevers', '/straightarmplanks', '/bentarmplanks', '/straightarmwallplanks', '/bentarmwallplanks', '/elbowlevergrip', '/diagonalelbowlevers', '/wallelbowlevers', '/singlelegelbowlevers', '/bentkneeelbowlevers', '/straddleelbowlevers', '/fullelbowlevers']
}

def yaml_export(path, movement):
    with open(path, 'w') as f:
        f.write('---\n')
        f.write('layout: movement\n')
        yaml.dump(data[mvt_n], f)
        f.write('---\n')


def parse_overview(response):
    mvt = {'overview': {}}
    for i, prog in enumerate(response.css('figure')):
        item = {}
        item['order'] = i + 1
        item['name'] = (prog.css('h3::text').get() or prog.css('h2::text').get()).split('-', 1)[-1].strip()
        item['thumbnail'] = prog.css('img::attr(src)').get()
        item['short_desc'] = prog.css('p::text').getall()[:-1] 
        mvt[item['name']] = item
    content = response.css('.content')[0]
    mvt['overview']['name'] = content.xpath('.//h1/text()').get() or content.xpath('.//h2/text()').get()
    mvt['overview']['desc'] = content.xpath('.//p/text()').get()
    mvt['overview']['video'] = content.xpath('.//a/@href').get()
    mvt['overview']['background'] = response.css('.section-background img::attr(src)').get()
    return mvt

def parse_progression(response):
    item = {}
    item['name'] = (response.css('h2::text').get() or response.css('h3::text').get())
    content = response.css('div .sqs-html-content')
    item['video'] = content[1].css('a::attr(href)').get()
    item['desc'] = [BeautifulSoup(e).get_text() for e in content[2].css('p').getall()]
    item['level'] = [e.strip() for e in content[3].css('h4::text').getall()]
    item['form'] = [BeautifulSoup(e).get_text() for e in content[4].css('p').getall()]
    item['tutorial'] = [BeautifulSoup(e).get_text() for e in content[5].css('p').getall()]
    item['prog_reg'] = [BeautifulSoup(e).get_text() for e in content[6].css('p').getall()[:-1]]
    return item

data = {}
for mvt_n in sorted(list(mvt_urls)):
    #if mvt_n not in ['Elbow Levers', 'Pushups', 'Lunges']:
    #    continue

    progs = mvt_urls[mvt_n]
    fetch(url_base + progs[0])
    try:
        mvt = parse_overview(response)
    except Exception as e:
        mvt = {}
        print(f'\n\n--> Pbm in {mvt_n} overview\n')
        print(traceback.format_exc())
        print()

    for i, prog_u in enumerate(progs[1:]):
        fetch(url_base + prog_u)
        try:
            item = parse_progression(response)
            item['order'] = i + 1

            if item['name'] not in mvt:
                mvt[item['name']] = item
            else:
                mvt[item['name']].update(item)
        except Exception as e:
            print(f'\n\n--> Pbm in {mvt_n} - {prog_u}\n')
            print(traceback.format_exc())
            print()
            continue
    if not mvt:
        continue
    if 'overview' in mvt:
        data[mvt_n] = mvt.pop('overview')
    else:
        data[mvt_n] = {}    
    data[mvt_n]['progression'] = sorted(mvt.values(), key=lambda x: x['order'])
    
    yaml_export(f'_movement/{mvt_n.lower()}.md', data[mvt_n])

with open('data.json', 'w') as f:
    json.dump(data, f)

# videos : https://github.com/shinosteph/calisthenics-routine/tree/main/media
#