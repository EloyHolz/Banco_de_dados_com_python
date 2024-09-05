import pandas as pd
import psycopg2

# Ler a planilha e substituir espaços em branco nos nomes das colunas
Sheetl_df = pd.read_excel("COMPILADO PLANILHA VARREDURA - GILMAR ARAUJO DA COSTA.xlsx")
Sheetl_df.columns = Sheetl_df.columns.str.strip().str.replace(' ', '_')

# Substituir valores em branco por None (equivalente a NULL no PostgreSQL)
Sheetl_df = Sheetl_df.replace(r'^\s*$', None, regex=True)

Sheetl_df = Sheetl_df.astype(object).where(pd.notnull(Sheetl_df), None)

db_host = 'localhost'
db_user = 'postgres'
db_password = 'senha'
db_name = 'banco'
db_port = 5432  # Default is 5432

# Abrir conexão com o banco de dados
conn = psycopg2.connect(
    host=db_host,
    user=db_user,
    password=db_password,
    dbname=db_name,
    port=db_port,
)

# Criar um cursor
cur = conn.cursor()

# Loop para inserir dados
for i, row in Sheetl_df.iterrows():
    print(Sheetl_df.columns)
    numero_de_integracao = Sheetl_df.loc[i, 'Nº_DE_INTEGRAÇÃO']
    nome_autor = Sheetl_df.loc[i, 'ENVOLVIDO']
    numero_processo = Sheetl_df.loc[i, 'PROCESSO_JUDICIAL']
    autor_falecido = Sheetl_df.loc[i, 'AUTOR_FALECIDO']
    peticao_generica = Sheetl_df.loc[i, 'PETIÇÃO_GENÉRICA?']
    conciliacao_ou_justicagratuita = Sheetl_df.loc[i, 'DISPENSA_CONCILIAÇÃO__E/OU_PEDE_JUSTIÇA_GRATUITA?']
    analfabeto = Sheetl_df.loc[i, 'ANALFABETO?_(ASSINADO_COM_DEDO?)']
    testemunha_1 = Sheetl_df.loc[i, 'SE_ANALFABETO:_TESTEMUNHA_1_(PROCURAÇÃO_E/OU_DECLARAÇÃO)']
    testemunha_2 = Sheetl_df.loc[i, 'SE_ANALFABETO:_TESTEMUNHA_2_(PROCURAÇÃO_E/OU_DECLARAÇÃO)']
    comprovante_declaracao = Sheetl_df.loc[i, 'COMPROVANTE_OU_DECLARAÇÃO']
    existe_nome_terceiro = Sheetl_df.loc[i, 'NOME_DE_TERCEIRO?']
    nome_terceiro = Sheetl_df.loc[i, 'SE_SIM,_QUAL_O_NOME_DO_TERCEIRO?']
    numero_medidor = Sheetl_df.loc[i, 'NÚMERO_DA_LINHA/MEDIDOR/HIDRÔMETRO']
    matricula_cliente = Sheetl_df.loc[i, 'CÓDIGO_DO_CLIENTE/USUÁRIO/MATRÍCULA']
    numero_contrato = Sheetl_df.loc[i, 'NÚMERO_DO_CONTRATO/CONTA']
    numero_nota_fiscal = Sheetl_df.loc[i, 'NÚMERO_DA_FATURA/NOTA_FISCAL']
    numero_debito_automatico = Sheetl_df.loc[i, 'CÓDIGO_DÉBITO_AUTOMÁTICO']
    status_processual = Sheetl_df.loc[i, 'STATUS_PROCESSUAL']
    multa_ou_mafe = Sheetl_df.loc[i, 'HÁ_DECISÕES_COM_APLICAÇÃO_DE_MULTA_POR_LITIGÂNCIA_DE_MÁ-FÉ_A_PARTE_OU_CAUSÍDICO?']
    oficio = Sheetl_df.loc[i, 'HÁ_DECISÕES_COM_EXPEDIÇÃO_DE_OFÍCIO?']
    observacoes = Sheetl_df.loc[i, 'OBSERVAÇÕES']
    cpf_cnpj = Sheetl_df.loc[i, 'CPF_CNPJ']
    ajuizamento = Sheetl_df.loc[i, 'AJUIZAMENTO']
    subtipo_acao = Sheetl_df.loc[i, 'SUBTIPO_ACAO']
    orgao_julgador = Sheetl_df.loc[i, 'ORGAO_JULGADOR']
    comarca = Sheetl_df.loc[i, 'COMARCA']
    uf = Sheetl_df.loc[i, 'UF']
    advogado_da_parte = Sheetl_df.loc[i, 'ADVOGADO_PARTE']

    # Montar a consulta SQL para inserir dados na tabela
    sql = """INSERT INTO intelijonas (numero_de_integracao, nome_autor, numero_processo, autor_falecido, 
    peticao_generica, conciliacao_ou_justicagratuita, analfabeto, testemunha_1, testemunha_2, comprovante_declaracao, 
    existe_nome_terceiro, nome_terceiro, numero_medidor, matricula_cliente, numero_contrato, numero_nota_fiscal, 
    numero_debito_automatico, status_processual, multa_ou_mafe, oficio, observacoes, cpf_cnpj, ajuizamento, 
    subtipo_acao, orgao_julgador, comarca, uf, advogado_da_parte) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

    # Executar a consulta com tratamento de exceções
    try:
        cur.execute(sql, (numero_de_integracao,
                          nome_autor,
                          numero_processo,
                          autor_falecido,
                          peticao_generica,
                          conciliacao_ou_justicagratuita,
                          analfabeto,
                          testemunha_1,
                          testemunha_2,
                          comprovante_declaracao,
                          existe_nome_terceiro,
                          nome_terceiro,
                          numero_medidor,
                          matricula_cliente,
                          numero_contrato,
                          numero_nota_fiscal,
                          numero_debito_automatico,
                          status_processual,
                          multa_ou_mafe,
                          oficio,
                          observacoes,
                          cpf_cnpj,
                          ajuizamento,
                          subtipo_acao,
                          orgao_julgador,
                          comarca,
                          uf,
                          advogado_da_parte))
        conn.commit()  # Confirmar a transação
    except Exception as e:
        print(f"Erro ao inserir dados: {e}")
        conn.rollback()  # Reverter a transação em caso de erro

# Imprimir as tabelas
cur.execute("SELECT table_name FROM information_schema.tables WHERE table_schema='public'")
tables = cur.fetchall()
for table in tables:
    print(table)

# Fechar a conexão
cur.close()
conn.close()
