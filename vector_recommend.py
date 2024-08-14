import streamlit as st

def show_vector():
    st.title("Vector Recommend")

    st.write("""
    The **4x CPU** is a 4-bit digital processor designed to execute a set of six distinct instructions encoded in binary. It reads instructions from left to right, simplifying the translation process, although the CPU internally inverts the instructions for execution.

    ### Instruction Set

    Each instruction consists of 4 bits followed by a '1'. If an instruction requires data, the data in binary is written before the instruction.

    1. **Wait/Null (00001)**: 
    - This command either clears the 6-bit register or passes an empty instruction to delay the next operation by one clock cycle.

    2. **Reset (10011)**: 
    - Resets the processor to its default state.

    3. **Store (10101)**: 
    - Stores 4 bits of data in SRAM. The data is written before the store command.
    - **Example**: To store the value 7: `1110 10101`. (In this case, `1110` is the binary representation of 7, read from left to right.)

    4. **Read (01011)**: 
    - Reads and displays the data stored in SRAM.

    5. **Add (11001)**: 
    - Adds two numbers and displays the result but does not store the result in SRAM.
    - **Example**: `11001` (3) + `1110` (7) = `0101` (10)

    6. **S-Add (11101)**: 
    - Adds two numbers and stores the result in SRAM.
""")
    st.subheader("Image View")
    st.image("4cpu.png", width=300,caption="4-bit Corporal Proccessing unit (Named after the Designers Internet Alias)")
