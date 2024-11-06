---
title: Definir Privilégios, Criptografar e Descriptografar Arquivo PDF 
linktitle: Criptografar e Descriptografar Arquivo PDF
type: docs
weight: 20
url: pt/java/set-privileges-encrypt-and-decrypt-pdf-file/
keywords: criptografar pdf,proteger pdf com senha,descriptografar pdf,java
description: Criptografar Arquivo PDF com Java usando Diferentes Tipos de Criptografia e Algoritmos. Além disso, descriptografar Arquivos PDF usando Senha do Proprietário.
lastmod: "2021-12-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Definir Privilégios em um Arquivo PDF Existente

Para definir privilégios em um arquivo PDF, crie um objeto da classe DocumentPrivilege e especifique os direitos que você deseja aplicar ao documento.
 Uma vez que os privilégios tenham sido definidos, passe este objeto como um argumento para o método [Encrypt](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#encrypt-java.lang.String-java.lang.String-com.aspose.pdf.facades.DocumentPrivilege-int-boolean-) do objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document). O trecho de código a seguir mostra como definir os privilégios de um arquivo PDF.

```java
  public static void SetPrivilegesOnExistingPDF()
  {
   // Carregar um arquivo PDF de origem
   Document document = new Document(_dataDir + "input.pdf");

   // Instanciar objeto de Privilégios do Documento
   // Aplicar restrições em todos os privilégios
   DocumentPrivilege documentPrivilege = DocumentPrivilege.getForbidAll();
   // Permitir apenas leitura de tela
   documentPrivilege.setAllowScreenReaders(true);
   // Criptografar o arquivo com senha de Usuário e Proprietário.
   // É necessário definir a senha, para que uma vez que o usuário visualize o arquivo com a senha de usuário,
   // Apenas a opção de leitura de tela esteja habilitada
   document.encrypt("user", "owner", documentPrivilege, CryptoAlgorithm.AESx128, false);
   // Salvar documento atualizado
   document.save(_dataDir + "SetPrivileges_out.pdf");
  }
```

## Criptografar Arquivo PDF usando Diferentes Tipos e Algoritmos de Criptografia

Você pode usar o método [Encrypt](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#encrypt-java.lang.String-java.lang.String-int-int-) do objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) para criptografar um arquivo PDF. Você pode passar a senha do usuário, a senha do proprietário e as permissões para o método [Encrypt](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#encrypt-java.lang.String-java.lang.String-int-int-). Além disso, você pode passar qualquer valor do enum [CryptoAlgorithm](https://reference.aspose.com/pdf/java/com.aspose.pdf/CryptoAlgorithm). Este enum fornece diferentes combinações de algoritmos de criptografia e tamanhos de chave. Você pode passar o valor de sua escolha. Finalmente, salve o arquivo PDF criptografado usando o método [save(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#save--) do objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

> Por favor, especifique diferentes senhas de usuário e proprietário ao criptografar o arquivo PDF.

O trecho de código a seguir mostra como criptografar arquivos PDF.

```java
public static void EncryptPDFFile() {
   // Carregar um arquivo PDF de origem
   Document document = new Document(_dataDir + "input.pdf");

   // Instanciar o objeto de Privilégios do Documento
   // Aplicar restrições em todos os privilégios
   DocumentPrivilege documentPrivilege = DocumentPrivilege.getForbidAll();
   // Permitir apenas leitura de tela
   documentPrivilege.setAllowScreenReaders(true);
   // Criptografar o arquivo com senha de Usuário e Proprietário.
   // Precisa definir a senha, para que uma vez que o usuário visualize o arquivo com a senha de usuário,
   // Apenas a opção de leitura de tela esteja habilitada
   document.encrypt("user", "owner", documentPrivilege, CryptoAlgorithm.AESx128, false);
   // Salvar documento atualizado
   document.save(_dataDir + "SetPrivileges_out.pdf");
  }
```

## Descriptografar Arquivo PDF usando Senha de Proprietário

Para descriptografar o arquivo PDF, primeiro você precisa criar um objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) e abrir o PDF usando a senha do proprietário.
 Após isso, você precisa chamar o método [Decrypt](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#decrypt--) do objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document). Finalmente, salve o arquivo PDF atualizado usando o método Save do objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document). O trecho de código a seguir mostra como descriptografar o arquivo PDF.

```java
public static void DecryptPDFFile() {
   // Abrir documento
   Document document = new Document(_dataDir + "Decrypt.pdf", "password");
   // Descriptografar PDF
   document.decrypt();

   // Salvar PDF atualizado
   document.save(_dataDir + "Decrypt_out.pdf");
  }
```

## Alterar Senha de um Arquivo PDF

Se você deseja alterar a senha de um arquivo PDF, primeiro precisa abrir o arquivo PDF usando a senha do proprietário com o objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document). Depois disso, você precisa chamar o método [ChangePasswords](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#changePasswords-java.lang.String-java.lang.String-java.lang.String-) do objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document). Você precisa passar a senha atual do proprietário junto com a nova senha do usuário e a nova senha do proprietário para este método. Finalmente, salve o arquivo PDF atualizado usando o método Save do objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

O snippet de código a seguir mostra como alterar a senha de um arquivo PDF.

```java
public static void ChangePassword_PDF_File() {
   // Abrir documento
   Document document = new Document(_dataDir+ "ChangePassword.pdf", "owner");
   // Alterar senha
   document.changePasswords("owner", "newuser", "newowner");
   // Salvar PDF atualizado
   document.save(_dataDir + "ChangePassword_out.pdf");
  }
```

## Como - determinar se o PDF de origem está protegido por senha

Aspose.PDF para Java oferece ótimas capacidades de lidar com documentos PDF. Quando usar a classe [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) do pacote com.aspose.pdf para abrir um documento PDF que está protegido por senha, precisamos fornecer as informações da senha como um argumento para o construtor do Document e, caso essa informação não seja fornecida, uma mensagem de erro é gerada. Na verdade, ao tentar abrir um arquivo PDF com o objeto Document, o construtor tenta ler o conteúdo do arquivo PDF e, caso a senha correta não seja fornecida, uma mensagem de erro é gerada (isso acontece para evitar o acesso não autorizado ao documento).

Ao lidar com arquivos PDF criptografados, você pode se deparar com o cenário em que estaria interessado em detectar se um PDF tem uma senha de abertura e/ou uma senha de edição. Às vezes, existem documentos que não requerem informações de senha ao abri-los, mas requerem informações para editar o conteúdo do arquivo. Portanto, para atender aos requisitos acima, a classe PdfFileInfo presente no pacote com.aspose.pdf.facades fornece os métodos que podem ajudar a determinar as informações necessárias.

### Obter informações sobre a segurança do documento PDF

PdfFileInfo contém três métodos para obter informações sobre a segurança do documento PDF.

1. O método getPasswordType() retorna o valor de enumeração PasswordType:
    1. PasswordType.None - o documento não está protegido por senha
    1. PasswordType.User - o documento foi aberto com a senha de usuário (ou senha de abertura do documento)
    1. PasswordType.Owner - o documento foi aberto com a senha de proprietário (ou permissões, edição)
    1. PasswordType.Inaccessible - o documento está protegido por senha, mas a senha é necessária para abri-lo enquanto uma senha inválida (ou nenhuma senha) foi fornecida.
1. O método hasOpenPassword() é usado para determinar se o arquivo de entrada requer uma senha ao abri-lo.  
1. O método hasEditPassword() é usado para determinar se o arquivo de entrada requer uma senha para editar seu conteúdo.

### Determinar a senha correta a partir de um Array

Às vezes, há a necessidade de determinar a senha correta a partir de um array de senhas e abrir o documento com a senha correta. O trecho de código a seguir demonstra as etapas para iterar através do array de senhas e tentar abrir o documento com a senha correta.

```java
public static void DetermineCorrectPasswordFromArray() {
     // Carregar arquivo PDF de origem
   PdfFileInfo info = new PdfFileInfo();
   info.bindPdf(_dataDir + "IsPasswordProtected.pdf");
   // Determinar se o PDF de origem está criptografado
   System.out.println("O arquivo está protegido por senha " + info.isEncrypted());
   String[] passwords = { "test", "test1", "test2", "test3", "sample" };
   for (int passwordcount = 0; passwordcount < passwords.length; passwordcount++)
   {
    try
    {
     Document doc = new Document(_dataDir + "IsPasswordProtected.pdf", passwords[passwordcount]);
     if (doc.getPages().size() > 0)
      System.out.println("Número de páginas no documento é = " + doc.getPages().size());
    }
    catch (InvalidPasswordException ex)
    {
     System.out.println("Senha = " + passwords[passwordcount] + " não é correta");
    }
   }
```