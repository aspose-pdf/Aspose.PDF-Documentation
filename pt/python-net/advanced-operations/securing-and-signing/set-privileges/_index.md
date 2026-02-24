---
title: Definir privilégios, criptografar e descriptografar PDF
linktitle: Criptografar e Descriptografar Arquivo PDF
type: docs
weight: 70
url: /pt/python-net/set-privileges-encrypt-and-decrypt-pdf-file/
description: Criptografe um arquivo PDF com Python usando diferentes tipos e algoritmos de criptografia. Também, descriptografe arquivos PDF usando a senha do proprietário.
lastmod: "2025-06-22"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Criptografar ou Descriptografar Arquivo PDF com Python
Abstract: Esta página de documentação explica como definir privilégios de documento, aplicar criptografia e descriptografar arquivos PDF usando Aspose.PDF para Python. Ela orienta os desenvolvedores na configuração de senhas de usuário e de proprietário, definindo restrições de acesso (como impressão, cópia ou edição). Exemplos de código ilustram como proteger conteúdo sensível e gerenciar a segurança de PDFs de forma eficaz em aplicações Python, garantindo acesso controlado e confidencialidade dos dados.
---

Gerenciar a segurança de documentos é essencial ao trabalhar com conteúdo sensível ou crítico para o negócio. Aspose.PDF para Python via .NET oferece uma API robusta para aplicar criptografia programaticamente, controlar o acesso por meio de permissões e descriptografar arquivos PDF protegidos.

Este artigo orienta desenvolvedores Python através de exemplos práticos para definir privilégios, aplicar e remover criptografia, alterar senhas e detectar estados de proteção — tudo dentro de um fluxo de trabalho de PDF.

Aspose.PDF para Python via .NET oferece aos desenvolvedores controle total sobre a segurança de PDFs:

**Definir privilégios** - Controle de acesso detalhado usando permissões.
**Criptografar arquivo** - Aplicar criptografia AES ou RC4 com senhas personalizadas.
**Descriptografar arquivo** - Remover a segurança usando a senha do proprietário.
**Alterar senhas** - Rotacionar ou atualizar credenciais sem alterar o conteúdo.
**Inspecionar segurança** - Detectar o status da criptografia ou os tipos de senha necessários.

## Definir privilégios em um arquivo PDF existente

Você pode restringir ou permitir operações específicas (por exemplo, impressão, cópia, preenchimento de formulários) atribuindo senhas de usuário e de proprietário juntamente com privilégios de acesso.

```python

    import aspose.pdf as ap

    path_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile

    # Open PDF document
    with ap.Document(path_infile) as document:
        # Instantiate Document Privileges object
        # Apply restrictions on all privileges
        document_privilege = ap.facades.DocumentPrivilege.forbid_all
        # Only allow screen reading
        document_privilege.allow_screen_readers = True
        # Encrypt the file with User and Owner password
        # Need to set the password, so that once the user views the file with user password
        # Only screen reading option is enabled
        document.encrypt("user", "owner", document_privilege, ap.CryptoAlgorithm.AE_SX128, False)
        # Save PDF document
        document.save(path_outfile)
```

## Criptografar arquivo PDF usando diferentes tipos e algoritmos de criptografia

Criptografar um PDF garante que apenas usuários com credenciais válidas possam abrir ou modificar o arquivo.

>Termos‑chave:

- Senha de usuário. Necessária para abrir o documento.

- Senha de proprietário. Necessária para alterar permissões ou remover a criptografia.

- Tamanho da chave. Use AE_SX128 para máxima segurança em fluxos de trabalho modernos.

O snippet de código a seguir mostra como criptografar arquivos PDF.

```python

    import aspose.pdf as ap

    path_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile

    # Open PDF document
    with ap.Document(path_infile) as document:
        # Encrypt PDF
        document.encrypt("user", "owner", ap.Permissions.EXTRACT_CONTENT, ap.CryptoAlgorithm.AE_SX128)
        # Save PDF document
        document.save(path_outfile)
```

## Descriptografar arquivo PDF usando senha de proprietário

Para remover a proteção por senha e restaurar o acesso completo:

1. Carrega o PDF criptografado usando a senha correta ('password' é a senha de usuário ou de proprietário).
1. Remove toda a proteção por senha e as configurações de criptografia do documento.
1. Salva o PDF agora desprotegido no arquivo de saída especificado.

```python

    import aspose.pdf as ap

    path_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile

    # Open PDF document with password
    with ap.Document(path_infile, "password") as document:
        # Decrypt PDF
        document.decrypt()
        # Save PDF document
        document.save(path_outfile)
```

## Alterar senha de um arquivo PDF

Para atualizar as credenciais de segurança (senhas de usuário e de proprietário) de um documento PDF preservando seu conteúdo e estrutura.

1. Abre o PDF usando a senha de proprietário existente ('owner'), que concede acesso total, incluindo permissão para alterar as configurações de segurança.
1. Substitui as senhas antigas por uma nova senha de usuário ('newuser') e uma nova senha de proprietário ('newowner').
1. Salva o PDF com as configurações de senha atualizadas.

```python

    import aspose.pdf as ap

    path_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile

    # Open PDF document with password
    with ap.Document(path_infile, "owner") as document:
        # Change password
        document.change_passwords("owner", "newuser", "newowner")
        # Save PDF document
        document.save(path_outfile)
```

## Como - determinar se o PDF de origem está protegido por senha

### Determinar a senha correta a partir de um array

Em alguns cenários, pode ser necessário identificar a senha correta a partir de uma lista de possíveis candidatas para acessar um PDF protegido. O snippet de código abaixo demonstra como verificar se um arquivo PDF está protegido por senha e, em seguida, tentar desbloqueá‑lo iterando por uma lista pré‑definida de senhas usando Aspose.PDF para Python via .NET.

O processo inclui:

1. Usar PdfFileInfo para detectar se o PDF está criptografado.
1. Tenta abrir o PDF com cada senha usando ap.Document().
1. Se for bem‑sucedido, imprime o número de páginas.
1. Caso contrário, captura a exceção e relata a senha que falhou.

```python

    import aspose.pdf as ap

    path_infile = self.data_dir + infile

    with ap.facades.PdfFileInfo() as pdf_file_info:
        # Bind PDF document
        pdf_file_info.bind_pdf(path_infile)
        # Determine if the source PDF is encrypted
        print("File is password protected " + str(pdf_file_info.is_encrypted))

        passwords = ["test", "test1", "test2", "test3", "sample"]

        for password_index in range(len(passwords)):
            try:
                with ap.Document(path_infile, passwords[password_index]) as document:
                    if len(document.pages) > 0:
                        print("Number of Pages in document are = " + str(len(document.pages)))
                    password_index = password_index + 1
            except Exception as e:
                print("Password = " + passwords[password_index] + " is not correct")
                password_index = password_index + 1
```


