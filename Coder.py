import tkinter.filedialog as fd
from PIL import Image

code = []
print('Что вы хотите сделать?')
print('1 - Закодировать текст в изображение (нужно будет выбрать .txt файл)')
print('2 - Прочитать текст из изображения (нужно будет выбрать .png файл)')

encode_dict = {'000': '0',
               '001': '1',
               '002': '2',
               '003': '3',
               '004': '4',
               '005': '5',
               '006': '6',
               '007': '7',
               '010': '8',
               '011': '9',
               '012': 'a',
               '013': 'b',
               '014': 'c',
               '015': 'd',
               '016': 'e',
               '017': 'f',
               '020': 'g',
               '021': 'h',
               '022': 'i',
               '023': 'j',
               '024': 'k',
               '025': 'l',
               '026': 'm',
               '027': 'n',
               '030': 'o',
               '031': 'p',
               '032': 'q',
               '033': 'r',
               '034': 's',
               '035': 't',
               '036': 'u',
               '037': 'v',
               '040': 'w',
               '041': 'x',
               '042': 'y',
               '043': 'z',
               '044': 'A',
               '045': 'B',
               '046': 'C',
               '047': 'D',
               '050': 'E',
               '051': 'F',
               '052': 'G',
               '053': 'H',
               '054': 'I',
               '055': 'J',
               '056': 'K',
               '057': 'L',
               '060': 'M',
               '061': 'N',
               '062': 'O',
               '063': 'P',
               '064': 'Q',
               '065': 'R',
               '066': 'S',
               '067': 'T',
               '070': 'U',
               '071': 'V',
               '072': 'W',
               '073': 'X',
               '074': 'Y',
               '075': 'Z',
               '076': 'а',
               '077': 'б',
               '100': 'в',
               '101': 'г',
               '102': 'д',
               '103': 'е',
               '104': 'ё',
               '105': 'ж',
               '106': 'з',
               '107': 'и',
               '110': 'й',
               '111': 'к',
               '112': 'л',
               '113': 'м',
               '114': 'н',
               '115': 'о',
               '116': 'п',
               '117': 'р',
               '120': 'с',
               '121': 'т',
               '122': 'у',
               '123': 'ф',
               '124': 'х',
               '125': 'ц',
               '126': 'ч',
               '127': 'ш',
               '130': 'щ',
               '131': 'ъ',
               '132': 'ы',
               '133': 'ь',
               '134': 'э',
               '135': 'ю',
               '136': 'я',
               '137': 'А',
               '140': 'Б',
               '141': 'В',
               '142': 'Г',
               '143': 'Д',
               '144': 'Е',
               '145': 'Ё',
               '146': 'Ж',
               '147': 'З',
               '150': 'И',
               '151': 'Й',
               '152': 'К',
               '153': 'Л',
               '154': 'М',
               '155': 'Н',
               '156': 'О',
               '157': 'П',
               '160': 'Р',
               '161': 'С',
               '162': 'Т',
               '163': 'У',
               '164': 'Ф',
               '165': 'Х',
               '166': 'Ц',
               '167': 'Ч',
               '170': 'Ш',
               '171': 'Щ',
               '172': 'Ъ',
               '173': 'Ы',
               '174': 'Ь',
               '175': 'Э',
               '176': 'Ю',
               '177': 'Я',
               '200': '.',
               '201': ',',
               '202': ':',
               '203': '!',
               '204': '?',
               '205': '-',
               '206': '+',
               '207': '_',
               '210': ' ',
               '211': '/',
               '212': '\\',
               '213': '*',
               '214': '(',
               '215': ')',
               '216': "'",
               '217': '"',
               '220': '%',
               '221': '@',
               '222': '#',
               '223': '№',
               '224': '$',
               '225': '^',
               '226': '&',
               '227': '=',
               '230': '|',
               '231': '<',
               '232': '>',
               '233': '[',
               '234': ']',
               '235': '{',
               '236': '}',
               '237': '`',
               '240': '~',
               '241': '',
               '242': '',
               '243': '',
               '244': '',
               '245': '',
               '246': '',
               '247': '',
               '250': '',
               '251': '',
               '252': '',
               '253': '',
               '254': '',
               '255': '',
               '256': '',
               '257': '',
               '260': '',
               '261': '',
               '262': '',
               '263': '',
               '264': '',
               '265': '',
               '266': '',
               '267': '',
               '270': '',
               '271': '',
               '272': '',
               '273': '',
               '274': '',
               '275': '',
               '276': '',
               '277': '',
               '300': '',
               '301': '',
               '302': '',
               '303': '',
               '304': '',
               '305': '',
               '306': '',
               '307': '',
               '310': '',
               '311': '',
               '312': '',
               '313': '',
               '314': '',
               '315': '',
               '316': '',
               '317': '',
               '320': '',
               '321': '',
               '322': '',
               '323': '',
               '324': '',
               '325': '',
               '326': '',
               '327': '',
               '330': '',
               '331': '',
               '332': '',
               '333': '',
               '334': '',
               '335': '',
               '336': '',
               '337': '',
               '340': '',
               '341': '',
               '342': '',
               '343': '',
               '344': '',
               '345': '',
               '346': '',
               '347': '',
               '350': '',
               '351': '',
               '352': '',
               '353': '',
               '354': '',
               '355': '',
               '356': '',
               '357': '',
               '360': '',
               '361': '',
               '362': '',
               '363': '',
               '364': '',
               '365': '',
               '366': '',
               '367': '',
               '370': '',
               '371': '',
               '372': '',
               '373': '',
               '374': '',
               '375': '',
               '376': '',
               '377': '',
               '400': '',
               '401': '',
               '402': '',
               '403': '',
               '404': '',
               '405': '',
               '406': '',
               '407': '',
               '410': '',
               '411': '',
               '412': '',
               '413': '',
               '414': '',
               '415': '',
               '416': '',
               '417': '',
               '420': '',
               '421': '',
               '422': '',
               '423': '',
               '424': '',
               '425': '',
               '426': '',
               '427': '',
               '430': '',
               '431': '',
               '432': '',
               '433': '',
               '434': '',
               '435': '',
               '436': '',
               '437': '',
               '440': '',
               '441': '',
               '442': '',
               '443': '',
               '444': '',
               '445': '',
               '446': '',
               '447': '',
               '450': '',
               '451': '',
               '452': '',
               '453': '',
               '454': '',
               '455': '',
               '456': '',
               '457': '',
               '460': '',
               '461': '',
               '462': '',
               '463': '',
               '464': '',
               '465': '',
               '466': '',
               '467': '',
               '470': '',
               '471': '',
               '472': '',
               '473': '',
               '474': '',
               '475': '',
               '476': '',
               '477': '',
               '500': '',
               '501': '',
               '502': '',
               '503': '',
               '504': '',
               '505': '',
               '506': '',
               '507': '',
               '510': '',
               '511': '',
               '512': '',
               '513': '',
               '514': '',
               '515': '',
               '516': '',
               '517': '',
               '520': '',
               '521': '',
               '522': '',
               '523': '',
               '524': '',
               '525': '',
               '526': '',
               '527': '',
               '530': '',
               '531': '',
               '532': '',
               '533': '',
               '534': '',
               '535': '',
               '536': '',
               '537': '',
               '540': '',
               '541': '',
               '542': '',
               '543': '',
               '544': '',
               '545': '',
               '546': '',
               '547': '',
               '550': '',
               '551': '',
               '552': '',
               '553': '',
               '554': '',
               '555': '',
               '556': '',
               '557': '',
               '560': '',
               '561': '',
               '562': '',
               '563': '',
               '564': '',
               '565': '',
               '566': '',
               '567': '',
               '570': '',
               '571': '',
               '572': '',
               '573': '',
               '574': '',
               '575': '',
               '576': '',
               '577': '',
               '600': '',
               '601': '',
               '602': '',
               '603': '',
               '604': '',
               '605': '',
               '606': '',
               '607': '',
               '610': '',
               '611': '',
               '612': '',
               '613': '',
               '614': '',
               '615': '',
               '616': '',
               '617': '',
               '620': '',
               '621': '',
               '622': '',
               '623': '',
               '624': '',
               '625': '',
               '626': '',
               '627': '',
               '630': '',
               '631': '',
               '632': '',
               '633': '',
               '634': '',
               '635': '',
               '636': '',
               '637': '',
               '640': '',
               '641': '',
               '642': '',
               '643': '',
               '644': '',
               '645': '',
               '646': '',
               '647': '',
               '650': '',
               '651': '',
               '652': '',
               '653': '',
               '654': '',
               '655': '',
               '656': '',
               '657': '',
               '660': '',
               '661': '',
               '662': '',
               '663': '',
               '664': '',
               '665': '',
               '666': '',
               '667': '',
               '670': '',
               '671': '',
               '672': '',
               '673': '',
               '674': '',
               '675': '',
               '676': '',
               '677': '',
               '700': '',
               '701': '',
               '702': '',
               '703': '',
               '704': '',
               '705': '',
               '706': '',
               '707': '',
               '710': '',
               '711': '',
               '712': '',
               '713': '',
               '714': '',
               '715': '',
               '716': '',
               '717': '',
               '720': '',
               '721': '',
               '722': '',
               '723': '',
               '724': '',
               '725': '',
               '726': '',
               '727': '',
               '730': '',
               '731': '',
               '732': '',
               '733': '',
               '734': '',
               '735': '',
               '736': '',
               '737': '',
               '740': '',
               '741': '',
               '742': '',
               '743': '',
               '744': '',
               '745': '',
               '746': '',
               '747': '',
               '750': '',
               '751': '',
               '752': '',
               '753': '',
               '754': '',
               '755': '',
               '756': '',
               '757': '',
               '760': '',
               '761': '',
               '762': '',
               '763': '',
               '764': '',
               '765': '',
               '766': '',
               '767': '',
               '770': '',
               '771': '',
               '772': '',
               '773': '',
               '774': '',
               '775': '',
               '776': '',
               '777': ''}

filename = fd.askopenfilename(title="Открыть файл")
if filename:
    if '.png' in filename:
        image = Image.open(filename)
        for i in range(image.height):
            for j in range(image.width):
                pixel = image.getpixel((j, i))
                if pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0:
                    code.append('0')
                elif pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 255:
                    code.append('1')
                elif pixel[0] == 0 and pixel[1] == 255 and pixel[2] == 0:
                    code.append('2')
                elif pixel[0] == 255 and pixel[1] == 0 and pixel[2] == 0:
                    code.append('3')
                elif pixel[0] == 0 and pixel[1] == 255 and pixel[2] == 255:
                    code.append('4')
                elif pixel[0] == 255 and pixel[1] == 255 and pixel[2] == 0:
                    code.append('5')
                elif pixel[0] == 255 and pixel[1] == 0 and pixel[2] == 255:
                    code.append('6')
                elif pixel[0] == 255 and pixel[1] == 255 and pixel[2] == 255:
                    code.append('7')
        code_cut = []
        i = 0
        while i + 3 < len(code):
            code_cut.append(code[i] + code[i + 1] + code[i + 2])
            i += 3
        output_string = []
        for let in code_cut:
            output_string.append(encode_dict[let])
        filename = filename.split('.')[0] + '.txt'
        out_txt = open(filename, 'w')
        out_txt.write(''.join(output_string))
        out_txt.close()

    elif '.txt' in filename:
        text = open(filename, 'r')
        input_text = text.read()
        code = []
        for let in input_text:
            for key in encode_dict:
                if encode_dict[key] == let:
                    b = list(key)
                    code.append(b[0])
                    code.append(b[1])
                    code.append(b[2])
                    break
        out_code = []
        for c in code:
            if c == '0':
                out_code.append((0, 0, 0))
            elif c == '1':
                out_code.append((0, 0, 255))
            elif c == '2':
                out_code.append((0, 255, 0))
            elif c == '3':
                out_code.append((255, 0, 0))
            elif c == '4':
                out_code.append((0, 255, 255))
            elif c == '5':
                out_code.append((255, 255, 0))
            elif c == '6':
                out_code.append((255, 0, 255))
            elif c == '7':
                out_code.append((255, 255, 255))

        w = h = int(len(out_code) ** 0.5) + 1
        image = Image.new('RGB', (w, h), (255, 255, 255))
        for i in range(w):
            for j in range(w):
                if w * i + j < len(out_code) - 1:
                    print(j, i)
                    pixel = image.putpixel((j, i), out_code[w * i + j])
        filename = filename.split('.')[0] + '.png'
        image = image.save(filename)

    print('Обработка завершена')
    print('Результат сохранён в', filename)
    wait = input('Нажмите ENTER чтобы закрыть программу')

