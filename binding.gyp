{
  'targets': [
    {
      'target_name': 'swisseph',
      'sources': [
        'src/swisseph.cc',
        'src/callback.cc',
        'src/date.cc',
        'src/pos.cc',
        'src/hel.cc'
      ],
      'dependencies': [
      	'deps/swisseph/swisseph.gyp:swisseph'
      ]
    }
  ]
}