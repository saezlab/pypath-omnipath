#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This is a script to exemplarise the usage of an adapter 
(pypath_biocypher_adapter) to create a BioCypher-compatible graph database 
from pypath objects. The mode of interaction with the graph in this case is
the passing of the locally instantiated Neo4j driver to the biocypher module, 
which resembles just one of multiple possible modes of interaction. Merging
nodes and edges with an UNWIND APOC call is safe, but relatively slow.

Copyright 2021, Heidelberg University Clinic

File author(s): Sebastian Lobentanzer
                ...

Distributed under GPLv3 license, see LICENSE.txt.

In the graph, we have the following components:
- nodes: an id (our primary identifier), a label (:Protein, :Complex ...), a
    dict of properties
    - NOTE: we also have a property called "label", which is the human-readable
        id of the node
- edges: source and target id (from primary identifiers), a label
    (:POST_TRANSLATIONAL ...), a dict of properties
- node labels are nouns written in CamelBack, edge labels are verbs written in
    UPPERCASE, properties are lowercase_with_underscore
    
Todo: 
    * duplicate relationships handling
    * progress bar?
    * batch processing
        - via APOC in parts
        - output csv file for admin import without safety

"""

import pypath.biocypher.adapter as adapter
    
bcy_adapter = adapter.BiocypherAdapter(wipe = True, db_name = 'neo4j')
bcy_adapter.build_network()

bcy_adapter = adapter.BiocypherAdapter(wipe = False, db_name = 'neo4j')


# def main():

#     # Instantialising the adapter class.
#     # We are creating a new database, so we wipe and initialise the local Neo4j
#     # instance. Set `wipe = False` if you want to update an existing BioCypher 
#     # graph.
#     bcy_adapter = adapter.BiocypherAdapter(wipe = True, db_name = 'neo4j')

#     # create another adapter without wipe to test meta node functionality
#     bcy_adapter = adapter.BiocypherAdapter(wipe = False, db_name = 'neo4j')


#     # Building a pypath network database:
#     bcy_adapter.build_network()


#     # Loading it into Neo4j:
#     # bcy_adapter.load_network()

#     # Does the following:
#     bcy_adapter.bcy.add_nodes(bcy_adapter.network.nodes.values())
#     # bcy_adapter.bcy.add_edges(bcy_adapter.network.generate_df_records())




# if __name__ == '__main__':

#     main()
