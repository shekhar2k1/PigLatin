# Piglatin
Project to translate paragraphs to piglatin.
As of now Vowels and consonants are taken literally and no library is being used
to determine actual pronunciation. I found cmudict library but did not have chance to
thoroughly try it out.

##Project download and Install
git clone https://github.com/shekhar2k1/PigLatin.git

cd PigLatin/

python setup.py install


##Server
sudo python run.py server --port 80


###Tests Run
python piglatintest/test.py

###HTTP usage
http://127.0.0.1/translate?text=Piglatintext.
