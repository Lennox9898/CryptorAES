# CryptorAES

So my Goal with this was to find out whats 
the Heaviest possible encryption you can can build 
on Python before its getting unstable.

turns out kyber post quantum is not. Got me the Feverdream to put every less vulnerable script into some fine tuned code wich turned out 
to be actual working relieable tool

which is apart from beeing ressource-hungry 

Cleaned and fixed version of the original cryptor_gui_kyber.py:
- Consistent 4-space indentation (no tabs).
- Removed broken PySimpleGUI event-loop fragment and replaced with a small CLI for key generation/testing.
- Preserves cryptographic helpers (Argon2id, HKDF, AES-GCM streaming, ChaCha20-Poly1305, Kyber/X25519 helpers).
- Gonna Throw a GUI in it soon and i think a version AES like 512 or 1000Something i dont know yet however its about to encrypt your data as for if im not breaking it in a moment
