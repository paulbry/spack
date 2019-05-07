# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

"""Schema for os-runner-mapping.yaml configuration file.

.. literalinclude:: ../spack/schema/os_runner_mapping.py
   :lines: 32-
"""

schema = {
    '$schema': 'http://json-schema.org/schema#',
    'title': 'Spack release builds os/runner mapping config file schema',
    'type': 'object',
    'additionalProperties': False,
    'patternProperties': {
        r'runners': {
            'type': 'object',
            'default': {},
            'patternProperties': {
                r'[\w\d\-_\.]+': {
                    'type': 'object',
                    'default': {},
                    'additionalProperties': False,
                    'properties': {
                        'image': {'type': 'string'},
                        'tags': {
                            'type': 'array',
                            'items': {'type': 'string'},
                        },

                        'setup_script': {'type': 'string'},
                        'variables': {
                            'type': 'object',
                            'patternProperties': {
                                r'\w[\w-]*': {'type': 'string'},
                            },
                        },
                        'compilers': {
                            'type': 'array',
                            'default': [],
                            'items': {
                                'type': 'object',
                                'default': {},
                                'additionalProperties': False,
                                'required': ['name'],
                                'properties': {
                                    'name': {'type': 'string'},
                                    'path': {'type': 'string'},
                                },
                            },
                        },
                    },
                },
            },
        },
    },
}
