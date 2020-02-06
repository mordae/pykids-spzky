from flask import Flask, request, jsonify, render_template

a = Flask(__name__, template_folder='.')

spzky = set()
spzky.add('ABC-1234')
spzky.add('BAATYRBEK')
spzky.add('PR1MATOR')

pokuty = set()


@a.route('/')
def index():
    if 'spz' in request.args:
        spzky.add(request.args['spz'])

    return render_template('objednavka.html', spzky=spzky, pokuty=pokuty)


@a.route('/kontrola')
def kontrola():
    if 'spz' not in request.args:
        return jsonify({'error': 'Chybi Ti SPZ'})

    if request.args['spz'] in spzky:
        return jsonify({'kontrola': 'platna'})

    pokuty.add(request.args['spz'])

    return jsonify({'kontrola': 'neplatna'})

if __name__ == '__main__':
    a.debug = True
    a.run()
