import argparse
import os


# Function to deduplicate the original file
def dedupe_file(input_file, output_file):
    try:
        seen_words = set()

        with open(input_file, 'r', encoding='utf-8') as infile, \
                open(output_file, 'w', encoding='utf-8') as outfile:

            for line in infile:
                words = line.split()
                deduped_words = []

                for word in words:
                    lower_word = word.lower()
                    if lower_word not in seen_words:
                        seen_words.add(lower_word)
                        deduped_words.append(word)

                outfile.write(' '.join(deduped_words) + '\n')

        print(f"Deduplication complete. Output saved to {output_file}")

    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


# Function to reset the deduplicated file.
def reset(deduped_file, output_file):
    try:
        with open(deduped_file, 'r', encoding='utf-8') as infile, \
                open(output_file, 'w', encoding='utf-8') as outfile:

            for line in infile:
                outfile.write(line)

        print(f"Reset complete. Output saved to {output_file}")

    except FileNotFoundError:
        print(f"Error: File '{deduped_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


def main():
    parser = argparse.ArgumentParser(description='File Deduplication Tool')
    parser.add_argument('--dedupe', help='Perform deduplication on the input file')
    parser.add_argument('--reset', help='Reset deduped file to a state closer to original')

    args = parser.parse_args()

    if args.dedupe:
        input_file = args.dedupe
        output_file = input_file.rsplit('.', 1)[0] + '-deduped.txt'

        dedupe_file(input_file, output_file)

        original_size = os.path.getsize(input_file)
        deduped_size = os.path.getsize(output_file)

        print(f"Success\nOriginal File: {input_file} Size: {original_size} bytes")
        print(f"Deduped File: {output_file} Size: {deduped_size} bytes")

    elif args.reset:
        deduped_file = args.reset
        output_file = deduped_file.rsplit('.', 1)[0] + '-reset.txt'

        reset(deduped_file, output_file)

        deduped_size = os.path.getsize(deduped_file)
        reset_size = os.path.getsize(output_file)

        print(f"Success\nDeduped File: {deduped_file} Size: {deduped_size} bytes")
        print(f"Reset File: {output_file} Size: {reset_size} bytes")

if __name__ == "__main__":
    main()
