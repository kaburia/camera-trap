import os
def encode_mp4_to_binary(mp4_path, binary_output_path):
    # Read the MP4 file as binary data
    with open(mp4_path, 'rb') as mp4_file:
        mp4_data = mp4_file.read()
    
    # Write the binary data to the output file
    with open(binary_output_path, 'wb') as binary_file:
        binary_file.write(mp4_data)
    
    print(f"Encoded {mp4_path} to {binary_output_path} as binary.")

# Example usage with paths
mp4_path = r"C:\Users\waith\OneDrive\Documents\5TH YEAR PROJECT\SHORT SHEEP VIDEO.mp4"
binary_output_path = r"C:\Users\waith\OneDrive\Documents\5TH YEAR PROJECT\EncodedMP4\example.bin"

encode_mp4_to_binary(mp4_path, binary_output_path)
