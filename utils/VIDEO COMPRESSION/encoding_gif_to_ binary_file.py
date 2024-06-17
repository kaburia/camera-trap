import PIL.Image
import zlib

def compress_gif_to_binary(input_path, output_path):
    # Open the GIF file with Pillow
    with PIL.Image.open(input_path) as img:
        # Convert the image to raw bytes
        raw_data = img.tobytes()
        
        # Compress the raw bytes using zlib
        compressed_data = zlib.compress(raw_data)
        
        # Write the compressed data to a binary file
        with open(output_path, 'wb') as binary_file:
            binary_file.write(compressed_data)

# Example usage with paths
input_path = r"C:\Users\waith\OneDrive\Documents\5TH YEAR PROJECT\SHEEP GIF FILE.gif"
output_path = r"C:\Users\waith\OneDrive\Documents\5TH YEAR PROJECT\CompressedGIFs\output.bin"
compress_gif_to_binary(input_path, output_path)
