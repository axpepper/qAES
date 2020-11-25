# qAES
Quantum AES

Our prior work has focused on the sbox, but we target a full implementation of AES in cirq. At this point in time, the implementation is skeletal. Choices of datatype implementations have been made, and rotword() has been implemented by reindexing.

To my knowledge, no implementation of AES has yet been written in Cirq, nor have I been able to find complete source-code for any quantum implementation. Implementing AES in Cirq would provide for useful resource estimates-- most novel, an estimate of circuit volume considering real world constraints such as error correction. Cirq also allows for many different parameters to be optimized at "compile-time", allowing for implementation flexibility as more knowledge is gained. 

In working with alexandru, we briefly discussed adding the s-box to a maintained list of interesting circuits. I imagine that a full qAES algorithm will be of similar or greater interest. At the very least, publishing source-code for qAES will provide greater access to an AES algorithm for the NISQ regime, allowing the community to test different compilation strategies using our algorithm. 

With accesssibility in mind, I've refrained from including the code for my s-box in its current form, due to its SAGEmath requirements. Eliminating these requirements will require using python-native libraries to compute linear algebra. Full python nativety will allow programmers and researchers to leverage higher-level debugging tools such as pycharm when analysing the circuit. 

Moving forward, I intend to include the best-known strategies for each component. Failing that, some sane, readable strategy should be sufficient. I've started by pasting links from research papers into docstrings for relevant functions. Please let me know if I'm missing any relevant prior-work.

-Alex
