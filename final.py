
import requests_cache
from flask import Flask ,render_template ,request ,jsonify
import json
import requests
import pymysql
import hashlib
import hmac

# ====================================================================
# Section A Connections
# ====================================================================
cone t =pymysql.connect(
    host='database-1.c10w78ziptph.us-east-1.rds.amazonaws.com',
    port=3306,
    user='admin',
    password='rishabh12345',
    db='database1')


# library_url_template='http://openlibrary.org/api/get?key=/b/OL1001932M'

# requests_cache.install_cache('library_api',backend='memory',expire_after=36000)

# ===============================================================================
# Section B Hash
# ================================================================================


def pwd_to_hash(pwd_str):
    ''' create a string with the hash value from a password string '''
    sha256 = hmac.new(pwd_str.encode('UTF-8'), digestmod=hashlib.sha256)
    hash_value = sha256.hexdigest()
    return hash_value


# ======================================================================================
# Section C CRUD Function
# ================================================================================

app = Flask(__name__)
# ---------------------------------------------------------------------
# till here we have just added all the formalities
# In this next section we are importing data from OpenlibraryAPI
# -----------------------------------------------------------------------
'''
@app.route('/books', methods=['GET'])
def get_all_books():
    print("----PART 1----")
    responda=requests.get(library_url_template)
    if responda.ok:
        return jsonify(responda.json())
    else:
        print(responda.reason)

'''

# --------------------------------------------------------------------------
# Now we are getting data from our cloud database
# --------------------------------------------------------------------------- b= 0
b = input("  Enter Password ")
b = pwd_to_hash(b)

if (b == "4d3ffa81150bb023b190db966426e7ffa29ebc05353e48c2a5bf1c35c074a5bf"):
    c = input("store username")


    @app.route('/library', methods=['GET'])
    def get_library():
        # print("-----PART 2-----")
        respondb = conet.cursor()
        respondb.execute("""SELECT*from database1.library """)
        info = respondb.fetchall()
        if len(info):
            if (c == "kapil" or c == "ankit"):

                return jsonify({'data': len(info)}, info[:]), 200
            else:
                return jsonify({'data': len(info)}, info[:len(info) // 2]), 200
        else:
            return jsonify({"Sorry but there seems to be no data :("}), 400


    # ---------------------------------------------------------
    # Now we use post function to create data
    # ----------------------------------------------------------

    # post=create
    @app.route('/library', methods=['POST'], )
    def post_library():
        # print("--------PART 3---------")
        respondc = conet.cursor()
        respondc.execute(
            """INSERT into database1.library(Title,Author,genre,publisher) VALUES ('Age of Wrath','Eraly,Abraham','history','Penguin')""")
        info = respondc.fetchall()
        if len(info):
            return jsonify({'data': len(info)}, info[:]), 200
        else:
            return jsonify({"Sorry but there seems to be no data :("}), 400


    # ----------------------------------------------------------------------------

    @app.route('/library', methods=['POST'], )
    def post_lib():
        # print("--------PART 4---------")
        respondd = conet.cursor()
        respondd.execute(
            """INSERT into database1.library(Title,Author,genre,publisher) VALUES ('The Trail','Kafka,Frank','sci-fi','Random House')""")
        info = respondd.fetchall()
        if len(info):
            return jsonify({'data': len(info)}, info[:]), 200
        else:
            return jsonify({"Sorry but there seems to be no data :("}), 400


    # -------------------------------------------------------------------------
    # Now we use put function to update the data
    # -------------------------------------------------------------------------
    # put=update#

    @app.route('/library', methods=['PUT'], )
    def put_library():
        # print("--------PART 5---------")
        responde = conet.cursor()
        responde.execute(
            """UPDATE database1.library SET Title='The Trial',genre='fiction' WHERE Publisher='Random House'""")
        info = responde.fetchall()
        if len(info):
            return jsonify({'data': len(info)}, info[:]), 200
        else:
            return jsonify({"Sorry but there seems to be no data :("}), 400


    # -------------------------------------------------------------------------
    # Now we use Delte function to delete the data
    # -------------------------------------------------------------------------

    @app.route('/library', methods=['DELETE'], )
    def delete_library():
        # print("--------PART 6---------")
        respondf = conet.cursor()
        respondf.execute("""DELETE FROM database1.library WHERE Publisher = 'Random House')""")
        info = respondf.fetchall()
        if len(info):
            return jsonify({'data': len(info)}, info[:]), 200
        else:
            return jsonify({"Sorry but there seems to be no data :("}), 400


    # ----------------------------------------------------------------------------
    # ======================================================================================================
    # Section D
    # ============================================================================================================

    if __name__ == "__main__":
        app.run(host='0.0.0.0')
        # app.run(host='0.0.0.0', ssl_context=('cert.pem', 'key.pem'))
        # Uncomment the above line to Run it on Https
else:
    print("Wrong Password!!!")
