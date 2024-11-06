---
title: Definir Privilégios, Criptografar e Descriptografar Arquivo PDF usando C++
linktitle: Criptografar e Descriptografar Arquivo PDF
type: docs
weight: 20
url: pt/cpp/set-privileges-encrypt-and-decrypt-pdf-file/
keywords: criptografar pdf,proteger pdf com senha,descriptografar pdf,c++
description: Criptografar Arquivo PDF com C++ usando Diferentes Tipos de Criptografia e Algoritmos. Além disso, descriptografar Arquivos PDF usando Senha do Proprietário.
lastmod: "2021-12-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Definir Privilégios em um Arquivo PDF Existente

Para definir privilégios em um arquivo PDF existente, o Aspose.PDF para C++ usa a classe [DocumentPrivilege](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.facades.document_privilege/) e especifica os direitos que você deseja aplicar ao documento. Uma vez que os privilégios tenham sido definidos, passe este objeto como um argumento para o método [Encrypt](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#af7adb89eb21ef5e78b2ef5ce04fabcd7) do objeto [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document).

O trecho de código a seguir mostra como definir os privilégios de um arquivo PDF.

```cpp
void SecuringAndSigning::SetPrivilegesOnExistingPDF() {
    // String para nome do caminho.
    String _dataDir("C:\\Samples\\");

    // Carregar um arquivo PDF de origem
    auto document = MakeObject<Document>(_dataDir + u"input.pdf");

    // Instanciar objeto de Privilégios de Documento

    // Aplicar restrições em todos os privilégios
    auto documentPrivilege = DocumentPrivilege::get_ForbidAll();
    // Permitir apenas leitura de tela
    documentPrivilege->set_AllowScreenReaders(true);

    // Criptografar o arquivo com senha de Usuário e Proprietário.
    // Precisa definir a senha, para que uma vez que o usuário visualize o arquivo com a senha do usuário,

    // Apenas a opção de leitura de tela é habilitada
    document->Encrypt(u"user", u"owner", documentPrivilege, CryptoAlgorithm::AESx128, false);

    // Salvar documento atualizado
    document->Save(_dataDir + u"SetPrivileges_out.pdf");
}
```

## Criptografar Arquivo PDF usando Diferentes Tipos de Criptografia e Algoritmos

Para criptografar o arquivo PDF use o método [Encrypt](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#af7adb89eb21ef5e78b2ef5ce04fabcd7) do objeto [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) para criptografar um arquivo PDF.


O trecho de código a seguir mostra como criptografar arquivos PDF.

```cpp
void SecuringAndSigning::EncryptPDFFile() {
    // String para nome do caminho.
    String _dataDir("C:\\Samples\\");

    // Carregar um arquivo PDF de origem
    auto document = MakeObject<Document>(_dataDir + u"input.pdf");

    // Instanciar objeto de Privilégios do Documento
    // Aplicar restrições em todos os privilégios
    auto documentPrivilege = DocumentPrivilege::get_ForbidAll();
    // Permitir apenas leitura de tela
    documentPrivilege->set_AllowScreenReaders(true);
    // Criptografar o arquivo com senha de Usuário e Proprietário.
    // É necessário definir a senha, para que uma vez que o usuário visualize o arquivo com a senha de usuário,
    // Apenas a opção de leitura de tela esteja habilitada
    document->Encrypt(u"user", u"owner", documentPrivilege, CryptoAlgorithm::AESx128, false);
    // Salvar documento atualizado
    document->Save(_dataDir + u"SetPrivileges_out.pdf");
}
```

## Descriptografar Arquivo PDF usando Senha do Proprietário

Para descriptografar o arquivo PDF, você primeiro precisa criar um objeto [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) e abrir o PDF usando a senha do proprietário. Depois disso, você precisa chamar o método [Decrypt](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#a9c26014465f4368edc6fc62b7ef3d76a).

```cpp
void SecuringAndSigning::DecryptPDFFile() {

// String para nome do caminho.

String _dataDir("C:\\Samples\\");

// Abrir documento

auto document = MakeObject<Document>(_dataDir + u"Decrypt.pdf", u"password");

// Descriptografar PDF

document->Decrypt();

// Salvar PDF atualizado

document->Save(_dataDir + u"Decrypt_out.pdf");
}
```

## Alterar Senha de um Arquivo PDF

Como seus PDFs podem conter informações importantes e confidenciais, eles devem permanecer seguros. Assim, pode ser necessário alterar a senha do seu documento PDF.

Se você quiser alterar a senha de um arquivo PDF, você primeiro precisa abrir o arquivo PDF usando a senha do proprietário com o objeto [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document). Depois disso, você precisa chamar o método [ChangePasswords](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#a9952055c2ac0afea827ce400b5ec951d).

O seguinte trecho de código mostra como alterar a senha de um arquivo PDF.
```cpp
void SecuringAndSigning::ChangePassword_PDF_File() {

// String for path name.

String _dataDir("C:\\Samples\\");


// Open document

auto document = MakeObject<Document>(_dataDir + u"ChangePassword.pdf", u"owner");

// Change password

document->ChangePasswords(u"owner", u"newuser", u"newowner");

// Save updated PDF

document->Save(_dataDir + u"ChangePassword_out.pdf");
}
```

## Como - determinar se o PDF de origem está protegido por senha

Um documento PDF criptografado com a senha do usuário não pode ser aberto sem uma senha. Precisamos determinar se o documento está protegido por senha antes de tentarmos abri-lo. Às vezes, existem documentos que não exigem informações de senha ao serem abertos, mas exigem informações para editar o conteúdo do arquivo. Portanto, para atender aos requisitos acima, a classe [PdfFileInfo](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.facades.pdf_file_info/) presente no Aspose.PDF.Facades fornece as propriedades que podem ajudar a determinar as informações necessárias.

### Obter informações sobre a segurança do documento PDF

PdfFileInfo contém três propriedades para obter informações sobre a segurança do documento PDF.

1. A propriedade PasswordType retorna o valor de enumeração PasswordType:
    - PasswordType.None - o documento não está protegido por senha
    - PasswordType.User - o documento foi aberto com a senha de usuário (ou de abertura do documento)
    - PasswordType.Owner - o documento foi aberto com a senha de proprietário (ou permissões, edição)

    - PasswordType.Inaccessible - o documento está protegido por senha, mas a senha é necessária para abri-lo enquanto uma senha inválida (ou nenhuma senha) foi fornecida.2. propriedade booleana HasOpenPassword - é usada para determinar se o arquivo de entrada requer uma senha ao abri-lo.
3. propriedade booleana HasEditPassword - é usada para determinar se o arquivo de entrada requer uma senha para editar seu conteúdo.

### Determinar a senha correta a partir de um Array

Às vezes, é necessário determinar a senha correta a partir de um array de senhas e abrir o documento com a senha correta. O trecho de código a seguir demonstra os passos para iterar através do array de senhas e tentar abrir o documento com a senha correta.

```cpp
void SecuringAndSigning::DetermineCorrectPasswordFromArray() {


// String para nome do caminho.

String _dataDir("C:\\Samples\\");


// Carregar arquivo PDF de origem

auto info = MakeObject<PdfFileInfo>(_dataDir + u"IsPasswordProtected.pdf");


// Determinar se o PDF de origem está criptografado

Console::WriteLine(u"Arquivo está protegido por senha {0}", info->get_IsEncrypted());

const int count = 5;

String passwords[count] = { u"test", u"test1", u"test2", u"owner", u"sample" };


for (int passwordcount = 0; passwordcount < count; passwordcount++)

{


try


{



auto document = MakeObject<Document>(_dataDir + u"IsPasswordProtected.pdf", passwords[passwordcount]);



auto pages = document->get_Pages()->get_Count();



if (pages > 0)




Console::WriteLine(u"Número de páginas no documento é = {0}", pages);


}


catch (Aspose::Pdf::InvalidPasswordException ex)


{



Console::WriteLine(u"Senha = {0} não está correta", passwords[passwordcount]);


}

}

Console::WriteLine(u"Teste concluído");
}
```