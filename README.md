# out
A simple module for coloured printing in python.

This is the c implementation.
All features besides basic colored printing are still missing.
This implementation is just for fun and for trying to get the most speed out of simple-out.

These are the results of my benchmark - results may vary:
print: ~ 50 ms / 100.000 outputs
out python without color: ~ 89 ms / 100.000 outputs
out python with color: ~ 90 ms / 100.000 outputs
out c without color: ~ 16 ms / 100.000 outputs
out c with color: ~ 17 ms / 100.000 outputs

For clarification: I have absolutly no idea, what this speed could be used for.
