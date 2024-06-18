import os
def decode_binary_to_mp4(binary_path, mp4_output_path):
    try:
        # Read the binary data from the binary file
        with open(binary_path, 'rb') as binary_file:
            binary_data = binary_file.read()

        # Write the binary data to an MP4 file
        with open(mp4_output_path, 'wb') as mp4_file:
            mp4_file.write(binary_data)

        print(f"Decoded {binary_path} to {mp4_output_path} as MP4.")

    except FileNotFoundError:
        print("File not found. Please check the file path and try again.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
binary_path = r"C:\Users\waith\OneDrive\Documents\5TH YEAR PROJECT\EncodedMP4\example.bin"
mp4_output_path = r"C:\Users\waith\OneDrive\Documents\5TH YEAR PROJECT\DecodedMP4\example_decoded.mp4"

decode_binary_to_mp4(binary_path, mp4_output_path)
