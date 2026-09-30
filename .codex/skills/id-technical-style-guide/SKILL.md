---
name: id-technical-style-guide
description: Use this skill when writing, translating, reviewing, or editing Indonesian programming documentation. It normalizes headings, step-by-step instructions, figure captions, terminology, API identifiers, UI labels, punctuation, and technical formatting to consistent technical Indonesian.
---

# Indonesian Technical Documentation Style

## Goal

Normalize Indonesian programming documentation to a clear, concise, consistent style suitable for developers.

Use **standard Indonesian (`id-ID`)** and established Indonesian technical terminology.

Use direct action-oriented language for procedures without unnecessary personal pronouns or excessive formality.

## Priority

When rules conflict, apply them in this order:

1. Project-specific localization instructions.
2. Approved Indonesian terminology glossary.
3. Product and API terminology.
4. This style guide.
5. General Indonesian writing conventions.

Never change API identifiers, commands, paths, filenames, macros, placeholders, or actual UI labels merely to satisfy a linguistic rule.

---

## 1. Identify the structural role first

Before rewriting text, determine whether it is:

- a task heading;
- a conceptual heading;
- a procedural step;
- a figure caption;
- a note or warning;
- explanatory prose;
- a UI label;
- an API or code identifier.

Do not normalize text mechanically without determining its structural role.

---

## 2. General writing style

Use concise and direct technical Indonesian.

Prefer clear active sentences.

Good:

- Metode ini menyimpan dokumen PDF.
- Contoh berikut mengonversi file PDF ke format DOCX.
- Kelas `Document` merepresentasikan dokumen PDF.
- Opsi ini menentukan kualitas gambar.

Avoid unnecessarily verbose introductory expressions.

Avoid:

- Penting untuk diperhatikan bahwa...
- Perlu diketahui bahwa...
- Seperti yang dapat kita lihat...
- Perlu dicatat bahwa...

when the information can be stated directly.

Instead of:

> Perlu diperhatikan bahwa metode ini memerlukan kata sandi.

Prefer:

> Metode ini memerlukan kata sandi.

---

## 3. Addressing the reader

Prefer direct instructions without explicit personal pronouns.

Good:

- Buka file PDF.
- Pilih halaman.
- Simpan dokumen.

Avoid unnecessary:

- Anda harus membuka file PDF.
- Anda perlu memilih halaman.
- Pengguna harus menyimpan dokumen.

Use `Anda` only when explicitly referring to the reader improves clarity.

Do not use informal pronouns such as `kamu` in professional programming documentation.

---

## 4. Headings

Use sentence-style capitalization.

Good:

- Mengonversi PDF ke DOCX
- Membuat dokumen PDF
- Mengekstrak teks dari PDF
- Mengatur opsi konversi
- Opsi konversi

Avoid English-style title capitalization.

Bad:

- Mengonversi PDF Ke DOCX
- Membuat Dokumen PDF
- Mengekstrak Teks Dari PDF
- Mengatur Opsi Konversi

Capitalize:

- the first word;
- proper names;
- product names;
- technologies;
- identifiers whose official spelling requires capitalization.

Do not normally add a period at the end of a heading.

Good:

> Membuat dokumen PDF

Bad:

> Membuat dokumen PDF.

---

## 5. Task headings

For task-oriented headings, use concise action forms with **meN- verbs**.

Good:

- Membuat dokumen PDF
- Menambahkan halaman
- Mengonversi PDF ke DOCX
- Mengekstrak gambar
- Mengatur opsi konversi
- Menyimpan dokumen

This distinguishes a task heading from a direct instruction.

Avoid mixing grammatical structures among sibling headings.

Bad:

- Pembuatan dokumen PDF
- Menambahkan halaman
- Cara mengatur font
- Penyimpanan dokumen

Prefer:

- Membuat dokumen PDF
- Menambahkan halaman
- Mengatur font
- Menyimpan dokumen

---

## 6. Conceptual headings

Use concise noun phrases for conceptual and reference sections.

Good:

- Prasyarat
- Opsi konversi
- Format yang didukung
- Batasan yang diketahui
- Pengelolaan font
- Struktur dokumen
- Referensi API
- Pengaturan lanjutan

Do not convert conceptual headings into action headings unless the section actually describes a procedure.

---

## 7. Step-by-step instructions

Use the Indonesian imperative form for explicit procedural steps.

For ordinary positive instructions, omit the `meN-` prefix where natural.

Good:

- Buat objek `Document`.
- Buka file PDF.
- Tambahkan halaman ke dokumen.
- Atur opsi konversi.
- Simpan dokumen.

Compare:

**Task heading**

> Membuat dokumen PDF

**Instruction**

> Buat objek `Document`.

Do not use heading-style verbs for explicit steps.

Avoid:

> Membuat objek `Document`.

Prefer:

> Buat objek `Document`.

---

## 8. Common instruction normalization

Normalize common procedural verbs as follows:

| Task/verb form | Preferred instruction |
|---|---|
| membuka | Buka |
| membuat | Buat |
| menambahkan | Tambahkan |
| mengatur | Atur |
| memilih | Pilih |
| menjalankan | Jalankan |
| menyimpan | Simpan |
| menghapus | Hapus |
| menginstal | Instal |
| menentukan | Tentukan |
| memeriksa | Periksa |
| mengonversi | Konversi |
| mengekstrak | Ekstrak |
| mengimpor | Impor |
| mengekspor | Ekspor |
| memanggil | Panggil |
| mendapatkan | Dapatkan |
| menggunakan | Gunakan |
| memasukkan | Masukkan |
| mengunduh | Unduh |
| mengunggah | Unggah |
| menyalin | Salin |

Follow the approved project glossary when another term is established.

Do not mechanically remove prefixes. Use the established imperative form of the verb.

---

## 9. Numbered procedures

Use numbered lists when actions must be performed in sequence.

Good:

1. Buat objek `Document`.
2. Tambahkan halaman ke dokumen.
3. Buat objek `TextFragment`.
4. Tambahkan teks ke halaman.
5. Simpan dokumen PDF.

Each numbered item should normally represent one primary action.

Avoid:

> 1. Buat dokumen, tambahkan halaman, atur font, tambahkan teks, lalu simpan file.

Split meaningful stages into separate steps.

Closely related actions may remain together when separating them would make the procedure unnecessarily fragmented.

---

## 10. Step punctuation

Write procedural steps as complete sentences.

Begin with a capital letter and end with a period.

Good:

1. Buka dokumen PDF.
2. Pilih halaman yang akan diproses.
3. Ekstrak teks dari halaman.

Bad:

1. buka dokumen
2. pemilihan halaman
3. ekstraksi teks

---

## 11. Context before action

When useful, establish where the action occurs before stating the action.

Good:

- Di menu **File**, pilih **Save As**.
- Di objek `PdfSaveOptions`, atur properti `Compliance`.
- Di Visual Studio, buka **NuGet Package Manager**.

If the documented UI is localized into Indonesian, use the exact localized labels instead.

Do not invent translated UI labels.

---

## 12. One primary action per step

Prefer one principal action per numbered step.

Good:

1. Buat objek `Document`.
2. Tambahkan halaman.
3. Simpan dokumen.

Closely related operations may be combined when they represent one logical task.

Acceptable:

> Buat objek `Document` dan teruskan jalur file ke konstruktornya.

Do not create unnecessary steps for every individual API call.

---

## 13. Explanations are not steps

Do not turn explanatory information into numbered steps unless the reader must perform an action.

Preferred:

1. Buat objek `Document`.

   Objek ini merepresentasikan dokumen PDF yang akan diproses.

The numbered sentence describes the action.

The following paragraph explains the object or result.

---

## 14. Figure captions

Use the following default pattern:

`Gambar N. Deskripsi`

Examples:

- Gambar 1. Struktur dokumen PDF
- Gambar 2. Opsi konversi
- Gambar 3. Hasil konversi
- Gambar 4. Konfigurasi proyek

Use sentence-style capitalization.

Keep captions concise and descriptive.

Avoid:

- Figure 3: Conversion Result
- Gambar 3. Hasil Konversi
- Gambar 3. Tangkapan layar
- Gambar 3. Contoh

A caption should identify what the figure communicates rather than merely identify it as an image.

---

## 15. Figure references

In running text, use:

- Lihat gambar 2.
- Gambar 3 menunjukkan hasil konversi.
- Konfigurasi proyek ditunjukkan pada gambar 4.

Use lowercase `gambar` in ordinary running text unless it begins a sentence or the publishing system specifies another convention.

---

## 16. API identifiers

Never translate:

- class names;
- method names;
- property names;
- namespaces;
- enum members;
- source-code variables;
- package names;
- command-line options;
- file extensions.

Good:

- Buat objek `Document`.
- Panggil metode `save()`.
- Atur properti `page_info`.
- Gunakan kelas `PdfSaveOptions`.

Bad:

- Buat objek `Dokumen`.
- Panggil metode `simpan()`.

Use inline code formatting for identifiers.

---

## 17. Grammar around API identifiers

Apply normal Indonesian grammar around technical identifiers.

Good:

- Buat instans `Document`.
- Gunakan metode `save()`.
- Atur properti `Compliance`.
- Akses koleksi `pages`.
- Teruskan objek ke `convert()`.

Do not alter identifiers to make them conform to Indonesian morphology.

---

## 18. Files, paths, commands, and values

Format literal filenames, paths, commands, extensions, and literal values as code.

Good:

- Buka `input.pdf`.
- Simpan hasil sebagai `output.pdf`.
- Jalankan `dotnet build`.
- Buka direktori `C:\Samples\PDF`.
- Atur nilainya ke `true`.

Do not translate literal values.

---

## 19. UI labels

Preserve the exact text displayed by the documented product.

If the UI displays:

> **Save As**

write:

> Pilih **Save As**.

If the localized UI displays:

> **Simpan sebagai**

write:

> Pilih **Simpan sebagai**.

Do not translate an English UI label merely because the surrounding documentation is Indonesian.

Documentation must match the actual interface.

---

## 20. Preferred Indonesian technical terminology

Use established Indonesian technical terminology consistently.

Examples:

| Concept | Preferred Indonesian |
|---|---|
| file | file |
| document | dokumen |
| directory | direktori |
| folder | folder |
| source code | kode sumber |
| database | basis data / database according to glossary |
| configuration | konfigurasi |
| settings | pengaturan |
| user | pengguna |
| user interface | antarmuka pengguna |
| library | pustaka / library according to glossary |
| method | metode |
| property | properti |
| parameter | parameter |
| application | aplikasi |
| object | objek |
| class | kelas |
| package | paket |
| server | server |
| client | klien |
| browser | peramban / browser according to glossary |

Some English-derived technical terms are common among Indonesian developers.

Do not replace established project terminology merely to maximize localization.

The approved glossary takes precedence.

---

## 21. Loanwords and English terminology

Indonesian programming documentation naturally contains English-derived technical terminology.

Translate established concepts when a natural Indonesian equivalent is expected by the project.

Examples:

- source code → kode sumber
- user → pengguna
- settings → pengaturan
- application → aplikasi

Preserve established technologies and product names:

- .NET
- Python
- Java
- JSON
- REST API
- NuGet
- GitHub

Avoid unnecessary mixed-language verbs.

Bad:

> Save dokumen.

Prefer:

> Simpan dokumen.

But preserve actual API identifiers:

> Panggil metode `save()`.

---

## 22. Standard Indonesian forms

Prefer standard Indonesian spelling in documentation.

Examples:

- objek
- metode
- parameter
- konfigurasi
- aplikasi
- aktivitas
- kualitas
- sistem

Avoid informal spellings, chat abbreviations, and unnecessary conversational forms.

Use terminology consistently according to the approved glossary.

---

## 23. Download and upload terminology

Prefer standard Indonesian verbs:

- `mengunduh` in descriptive prose;
- `unduh` in instructions;
- `mengunggah` in descriptive prose;
- `unggah` in instructions.

Examples:

Descriptive:

> Aplikasi mengunduh file dari server.

Instruction:

> Unduh file konfigurasi.

Descriptive:

> Aplikasi mengunggah dokumen ke server.

Instruction:

> Unggah dokumen.

Preserve **Download** or **Upload** when those are actual UI labels.

---

## 24. Negatives and warnings in procedures

Use `Jangan` for direct prohibitions.

Good:

> Jangan tutup aplikasi selama proses konversi.

> Jangan ubah nama file konfigurasi.

Avoid unnecessarily indirect prohibitions.

Less direct:

> Sebaiknya aplikasi tidak ditutup selama proses konversi.

Use the indirect form only when the statement is a recommendation rather than a strict prohibition.

---

## 25. Terminology consistency

Use one preferred term for one concept.

Do not randomly alternate among:

- pengguna / user;
- direktori / folder when referring to the same concept;
- pustaka / library;
- basis data / database;
- peramban / browser;
- konfigurasi / pengaturan when they refer to the same concept.

Different terms are acceptable when they represent genuinely different concepts.

The approved project glossary takes precedence.

---

## 26. Notes, tips, and warnings

Use consistent labels.

Recommended:

> **Catatan:** information that supplements the main text.

> **Tips:** optional advice or a more efficient approach.

> **Penting:** information necessary for successful completion.

> **Peringatan:** potential risk, destructive operation, security issue, or data loss.

Do not alternate labels without a semantic reason.

Example:

> **Catatan:** Opsi ini hanya tersedia untuk dokumen PDF/A.

> **Peringatan:** Operasi ini akan menghapus file yang ada.

---

## 27. Macros and placeholders

Never translate or modify macros and placeholders unless explicitly instructed.

Examples:

- `{{productName}}`
- `{{language}}`
- `{0}`
- `{filename}`
- `%PATH%`
- `${HOME}`

Good:

> Instal paket `{{productName}}`.

Bad:

> Instal paket `{{namaProduk}}`.

Preserve spelling, capitalization, braces, and delimiters exactly.

---

## 28. Parallel structure

Keep sibling headings grammatically parallel.

Good:

- Membuat dokumen
- Menambahkan halaman
- Mengatur font
- Menyimpan dokumen

Bad:

- Membuat dokumen
- Penambahan halaman
- Cara mengatur font
- Simpan dokumen

Keep procedural steps parallel:

- Buat...
- Tambahkan...
- Atur...
- Simpan...

---

## 29. Normalization examples

### Heading

Before:

> Cara Untuk Membuat Dokumen PDF.

After:

> Membuat dokumen PDF

### Instruction

Before:

> Membuat objek `Document`.

After:

> Buat objek `Document`.

### Unnecessary reader reference

Before:

> Anda harus membuka file PDF.

After:

> Buka file PDF.

### Impersonal instruction

Before:

> File PDF harus dibuka terlebih dahulu.

After:

> Buka file PDF terlebih dahulu.

Use the passive form only when the object or result is more important than the actor.

### Figure caption

Before:

> Figure 2: Conversion Result

After:

> Gambar 2. Hasil konversi

### API identifier

Incorrect:

> Panggil metode `simpan()`.

Correct:

> Panggil metode `save()`.

Only make this correction when `save()` is the actual API identifier.

### UI label

If the actual UI displays **Save As**, preserve it:

> Pilih **Save As**.

Do not change it to **Simpan sebagai** unless that is the actual UI label.

---

## 30. Agent decision order

When reviewing Indonesian technical documentation:

1. Determine the structural role of the text.
2. Preserve API identifiers, commands, paths, filenames, macros, placeholders, and actual UI labels.
3. Determine whether a heading describes a task or a concept.
4. Use `meN-` action forms for task headings.
5. Use concise noun phrases for conceptual headings.
6. Use direct imperative forms for procedural steps.
7. Avoid unnecessary `Anda` in instructions.
8. Apply sentence-style capitalization.
9. Preserve parallel grammatical structure.
10. Apply the approved Indonesian glossary.
11. Check figure-caption formatting.
12. Check punctuation and technical formatting.
13. Check terminology consistency.
14. Verify that technical literals were not translated.

Never normalize Indonesian documentation mechanically without determining context first.

---

## 31. Review checklist

Before completing an Indonesian technical-documentation task, verify:

- [ ] The target language is standard Indonesian (`id-ID`).
- [ ] Task headings use consistent action-oriented forms.
- [ ] Conceptual headings use concise noun phrases.
- [ ] Headings use sentence-style capitalization.
- [ ] Headings do not end with unnecessary periods.
- [ ] Procedural steps use direct imperative forms.
- [ ] Instructions avoid unnecessary `Anda`.
- [ ] Steps are complete sentences.
- [ ] Numbered steps contain clear actions.
- [ ] Sibling headings and steps use parallel structures.
- [ ] Figure captions follow `Gambar N. Deskripsi`.
- [ ] Figure captions describe their content.
- [ ] API identifiers have not been translated.
- [ ] Commands, filenames, paths, macros, and placeholders remain unchanged.
- [ ] UI labels match the actual product UI.
- [ ] Standard Indonesian spelling is used.
- [ ] Technical terminology is consistent.
- [ ] The approved glossary takes precedence.

## Core rule

**Use `meN-` action forms for task headings, direct imperative forms for procedural instructions, and descriptive noun phrases for figure captions.**

Example:

Heading:

> Membuat dokumen PDF

Step:

> Buat objek `Document`.

Figure:

> Gambar 1. Struktur dokumen PDF

Locale:

> `id-ID`