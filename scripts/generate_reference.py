#!/bin/bash
import os

absolute_path = "/home/filip/Documents/unity/Sandbox/Build/Sandbox_Data/Managed/"


def get_print_reference( name ):

    reference_lines = [
        f'<Reference Include="{ name }">\n',
        f'    <HintPath>../../Sandbox_Data/Managed/{ name }.dll</HintPath>\n',
        "</Reference>\n"
    ]

    return ''.join( str(x) for x in reference_lines )


def get_files_list( path, type = ".dll" ):

    list = []
    for x in os.listdir( path ):

        if x.endswith( type ):
            list.append( x.replace( type, '') )
    
    return list


references = ""
files = get_files_list( absolute_path )
for file in files:
    reference = get_print_reference( file )
    references += reference

print( references )