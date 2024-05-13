# Deduplication
 A command-line tool for deduplicating text files and resetting deduplicated files back to a state closer to the original.

# Requirements
 - Python 3.x
# Usage
1. **Deduplication Mode:**
   ```bash
    $ python file_deduplication.py --dedupe <input_file>
   ```

This command performs deduplication on the specified <input_file>. The deduplicated content will be saved to a new file named <input_file>-deduped.txt.

2. **Reset Mode:**
   ```bash
   $ python file_deduplication.py --reset <deduped_file>
   ```
This command resets a deduplicated file (<deduped_file>) back to a state closer to the original. The reset content will be saved to a new file named <deduped_file>-reset.txt.

# Command-line Arguments
 - --dedupe <input_file>: Specify the input file for deduplication.
 - --reset <deduped_file>: Specify the deduplicated file to reset.

Example
1. Deduplication
```bash
python file_deduplication.py --dedupe input.txt
```
This command will deduplicate input.txt and save the deduplicated content to input-deduped.txt.

2. Reset
```bash
python file_deduplication.py --reset input-deduped.txt
```
This command will reset input-deduped.txt back to a state closer to the original and save the result to input-deduped-reset.txt.

# Note
- The deduplication process is case-insensitive, treating words like "Project" and "project" as duplicates. 
- Ensure that you have the necessary permissions to read/write files in the specified directories. 
- Error messages will be displayed if the specified input files are not found or if any other issues occur during file operations.
# Limitations
- The tool is designed for text files and may not work optimally with binary files or files containing complex formatting. 
- Large input files may impact performance due to memory and processing constraints.

****