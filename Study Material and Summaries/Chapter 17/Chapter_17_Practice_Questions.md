# Chapter 17 Practice Questions

## Questions

1. What are some features Excel spreadsheets have that CSV spreadsheets don't?

2. How would you read a PDF file in binary mode?

3. What PyPDF2 function creates a PdfFileReader object?

4. How do you get the number of pages in a PDF file?

5. If a PdfFileReader object's PDF is encrypted with the password `swordfish`, what must you do before you can obtain Page objects from it?

6. What methods do you use to rotate a page?

7. What method returns a Page object for a page number?

8. What PdfFileWriter method will create a new PDF file?

9. What module must be imported to work with Word (.docx) files?

10. What two types of objects does the python-docx module provide?

11. What is the difference between a paragraph object and a run object?

12. How do you get a list of Paragraph objects for a Document object that's stored in a variable named `doc`?

13. What type of object has `bold`, `italic`, `underline`, and `strike` variables?

14. How do you make the text "Hello World" bold?

15. How do you make the text in a paragraph justified (aligned on both left and right sides)?

## Answers

1. Excel spreadsheets can have values of data types other than strings; cells can have different fonts, sizes, or color settings; can have multiline text in cells; cells can have borders or background colors; cells can be merged; formulas can be stored; charts, images can be embedded; multiple worksheets can exist; width and height settings per cell.

2. `open('filename.pdf', 'rb')`

3. `PyPDF2.PdfFileReader()`

4. Use the `numPages` attribute on a PdfFileReader object.

5. You must call `pdfReader.decrypt('swordfish')` before calling methods like `getPage()`.

6. `rotateClockwise()` and `rotateCounterClockwise()` methods.

7. The `getPage(pageNumber)` method returns a Page object.

8. The `write()` method creates a new PDF file.

9. The `docx` module (python-docx package).

10. Paragraph objects and Run objects.

11. A Paragraph object represents a paragraph of text. A Run object represents a continuous run of text within a paragraph with the same style/formatting.

12. `doc.paragraphs`

13. Run objects have these style variables.

14. Create a run with the text and set `run.bold = True`.

15. Set the paragraph's alignment by accessing `paragraph.alignment` and setting it to `docx.enum.text.WD_ALIGN_PARAGRAPH.JUSTIFY` or by using `add_paragraph()` with appropriate style.
