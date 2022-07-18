#def main():
while input:

    monopolyCode = input('Hello! What is the Monopoly code? Use Caps Lock   ')

    monopoly_pieces_needed = ['327CG' , '332DH' , '318BE' , '321AF' , '309AC' , '315CD' , '302BA' , 
    '308DB' , '365AP' , '362BO' , '358BN' , '353AM' , '335CI' , 
    '336DI' , '372DQ' , '374BR' , '379CS' , '381AT' , '341CJ' , '351CL' , '348DK' , '343EJ' , 
    '391CV' , '388DU' , '394BW' , '397EW' , '408AZ' , '411DZ' , '398AX' , '401DX' , 
    '416D$' , '417E$' , '403AY' , '404BY' , '419B#' , '420C#']

    monopoly_pieces_we_have = ['405CY' , '406DY' , '407EY' , '418A#' , '421D#' , '422E#' , '405CY' , '406DY' , '407EY' ,
    '393AW' , '395CW' , '396DW' , '399BX' , '400CX' , '402EX' , '409BZ' , '412EZ' , '414B$' , '415C$' , '349AL' , '350BL' ,
    '352DL' , '345AK' , '346BK' , '339AJ' , '340BJ' , '342DJ' , '344FJ' , '389AV' , '390BV' , '392DV' , '385AU' , '386BU' , 
    '387CU' , '377AS' , '378BS' , '380DS' , '382BT' , '383CT' , '384DT' , '359CN' , '360DN' , '354BM' , '355CM' , '356DM' , 
    '333AI' , '334BI' , '337EI' , '338FI' , '369AQ' , '370BQ' , '371CQ' , '373AR' , '375CR' , '376DR' , '366BP' , '368DP' ,
    '361AO' , '363CO' , '364DO' , '325AG' , '326BG' , '328DG' , '329AH' , '330BH' , '331CH' , '317AE' , '319CE' , '320DE' , 
    '322BF' , '323CF' , '310BC' , '311CC' , '312DC' , '313AD' , '314BD' , '316DD' , '301AA' , '304DA' , '306BB' , '307CB' ,
    '410CZ' , '347CK' , '413A$' , '367CP' , '324DF' , '303CA' , '305AB' , '357AN' ]

    if monopolyCode in monopoly_pieces_needed:     
        print('\n\tAdd it to the board!\n')
        
    elif monopolyCode in monopoly_pieces_we_have:
        print('\n\tWe already have this piece :-(\n')
    else: 
        print('\n\tInvalid code try again\n')





#if __name__ == '__main__':
#    main()
