import cx_Oracle
from table2Excel import write_cursor_to_excel

conn = cx_Oracle.connect('system/oracle@//localhost:49153/xe')

print('Conectado')

curs = conn.cursor()

curs.execute("""
-- Lista os atendimentos do Risk Assessment (CO330 - Conhecendo sua saúde - 7603)
SELECT
    SAIDA.ID_AUTO_ATENDIMENTO,
    ATD.DATA_HORA,
    OP.NR_CARTEIRINHA,
    FIS.NM_PESSOA,
    con.ddd,
    con.nr_telefone,
    con.e_mail,
    FIS.ID_PESSOA,
    FIS.DT_NASCIMENTO,

    -- Texto tratado das respostas    
    case substr(fi.vc_texto, 14, 12)
      when '<SPAN style=' then 'Agradecemos o envio das informacoes. Agora conhecemos um pouco mais sobre a sua saude e vamos orientar o cuidado certo para voce. Nossa equipe de saude entrara em contato para direcionar sua jornada de cuidados.'
      else 
                  REPLACE(      
                  REPLACE(      
                TRANSLATE(
                  REPLACE(
                  REPLACE(
                  REPLACE(
                  REPLACE(
                  REPLACE(
                  REPLACE(
                  REPLACE(
                  REPLACE(
                  REPLACE(FI.VC_TEXTO, 
                          '<FONT size=+0>', ''), 
                          '</FONT>', ''), 
                          '<P>', ''), 
                          '</P>', ''), 
                          'Ã', 'A'), 
                          'ã', 'a'), 
                          '<STRONG>', ''), 
                          '</STRONG>', ''), 
                          '<BR>', ''), 
                          '!@#$%^&*()', '          '),
                          '<FONT >', ''),
                          'nbsp;', '')
    end as RESPOSTA,
    
    RANK() OVER(PARTITION BY SAIDA.ID_AUTO_ATENDIMENTO ORDER BY SAIDA.ID_SAIDA_AUTO_ATENDIMENTO DESC) RNK
    
  -- Dados do questionário
  FROM AMESP.GLB_SAIDAS_AUTO_ATENDIMENTO SAIDA
  JOIN AMESP.GLB_AUTO_ATENDIMENTO ATD ON ATD.ID_AUTO_ATENDIMENTO = SAIDA.ID_AUTO_ATENDIMENTO
  JOIN AMESP.FLX_ITEM FI on fi.id_fluxo_item = saida.id_fluxo_item
  -- Dados do paciente
  JOIN AMESP.GLB_PESSOA_OPERADORA OP ON OP.ID_PESSOA_OPERADORA = ATD.ID_PESSOA_OPERADORA 
  JOIN AMESP.GLB_PESSOA_FISICA FIS ON FIS.ID_PESSOA = OP.ID_PESSOA
  left join amesp.glb_pessoa_contato con on con.id_pessoa = fis.id_pessoa

WHERE 
  -- Questionário 
  SAIDA.ID_PROTOCOLO = 7683 -- Adulto
  --SAIDA.ID_PROTOCOLO = 7723 -- Infantil
  -- Período da listagem
  AND ATD.DATA_HORA between
      TO_DATE('06/06/2021 00:00', 'DD/MM/YYYY hh24:mi') and
      TO_DATE('06/06/2021 23:59', 'DD/MM/YYYY hh24:mi')
      
--  and saida.id_auto_atendimento = 124785 --124912
ORDER BY SAIDA.ID_AUTO_ATENDIMENTO, RNK desc

/

""")
write_cursor_to_excel(curs, 'teste.xls', 'Relatório SM')
print('Relatório gerado com sucesso...')