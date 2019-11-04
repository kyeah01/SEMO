<template>
<div>
  <div>
    <h2>3. Responses</h2>
  </div>
  <div style="display: flex;" >
    <table class="Guide-ep-table">
      <thead>
        <tr>
          <th><h3>Response</h3></th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(item, index) in responses" :key="index">
          <th :class="[{ 'select-Ep-act' : is_activeEp === index }, 'select-Ep']" @click="epSelect(index)">
            <h3>
              <span class="btn" :class="{'btn--success' : item.status == '200', 'btn--danger' : (item.status == '401' || item.status == '404')}"></span>
              {{ item.status }}
            </h3>
          </th>
        </tr>
      </tbody>
    </table>

    <table class="Guide-ep-subTable">
      <thead>
        <tr>
          <th :class="[{ 'select-Lang-act' : is_activeLang === index}, 'select-Lang']" colspan="2" v-for="(item, index) in resData" :key="index" @click="langSelect(index, item.title)"><h3>{{ item.title }}</h3></th>
        </tr>
      </thead>
      <tbody class="resTable" v-if="is_activeLang===0">
        <tr class="Guide-ep-inputBox" colspan="8">
          <th>
            Object
          </th>
          <th>
            Type
          </th>
          <th>
            Reqiured
          </th>
        </tr>
        <tr v-for="(item, index) in objects" :key="index">
          <th>
            {{ item.title }}
          </th>
          <th>
            <span :class="{'tyColor-success' : item.type == 'Integer', 'tyColor-primary' : item.type == 'Boolean', 'tyColor-danger' : item.type == 'String'}">
              {{ item.type }}
            </span>
          </th>
          <th>
            <span class="btn" :class="{'btn--danger' : item.required == 'required', 'btn--tertiary' : item.required == 'optional'}"> {{ item.required }} </span>
          </th>
        </tr>
      </tbody>
      <tbody class="resTable" v-if="is_activeLang===1">
        <tr class="Guide-ep-inputBox" colspan="8">
          <th>
            <pre style="text-align:start; user-select: text; width:750px;">
{
  "adult": false,
  "backdrop_path": "/fCayJrkfRaCRCTh8GqN30f8oyQF.jpg",
  "belongs_to_collection": null,
  "budget": 63000000,
  "genres": [
    {
      "id": 18,
      "name": "Drama"
    }
  ],
  "homepage": "",
  "id": 550,
  "imdb_id": "tt0137523",
  "original_language": "en",
  "original_title": "Fight Club",
  "popularity": 0.5,
  "poster_path": null,
  "production_companies": [
    {
      "id": 508,
      "logo_path": "/7PzJdsLGlR7oW4J0J5Xcd0pHGRg.png",
      "name": "Regency Enterprises",
      "origin_country": "US"
    },
    {
      "id": 711,
      "logo_path": null,
      "name": "Fox 2000 Pictures",
      "origin_country": ""
    },
    {
      "id": 20555,
      "logo_path": null,
      "name": "Taurus Film",
      "origin_country": ""
    },
    {
      "id": 54050,
      "logo_path": null,
      "name": "Linson Films",
      "origin_country": ""
    },
    {
      "id": 54051,
      "logo_path": null,
      "name": "Atman Entertainment",
      "origin_country": ""
    },
    {
      "id": 54052,
      "logo_path": null,
      "name": "Knickerbocker Films",
      "origin_country": ""
    },
    {
      "id": 25,
      "logo_path": "/qZCc1lty5FzX30aOCVRBLzaVmcp.png",
      "name": "20th Century Fox",
      "origin_country": "US"
    }
  ],
  "production_countries": [
    {
      "iso_3166_1": "US",
      "name": "United States of America"
    }
  ],
  "release_date": "1999-10-12",
  "revenue": 100853753,
  "runtime": 139,
  "spoken_languages": [
    {
      "iso_639_1": "en",
      "name": "English"
    }
  ],
  "status": "Released",
  "tagline": "How much can you know about yourself if you've never been in a fight?",
  "title": "Fight Club",
  "video": false,
  "vote_average": 7.8,
  "vote_count": 3439
}
            </pre>
          </th>
        </tr>
      </tbody>
    </table>

  </div>
</div>
</template>

<script>
export default {
  name: 'APIGuideRes',
  data() {
    return {
      resData: [
        {title : "Schema"},
        {title : "Example"},
      ],
      responses: [
        { status: '200'},
        { status: '401'},
        { status: '404'},
      ],
      objects: [
        {title: "adult", type: "Boolean", required: "optional"},
        {title: "backdrop_path", type: "String", required: "optional"},
        {title: "budget", type: "Integer", required: "optional"},
        {title: "homepage", type: "String", required: "optional"},
        {title: "imdb_id", type: "String", required: "optional"},
        {title: "popularyty", type: "Integer", required: "optional"},
        {title: "overview", type: "Integer", required: "optional"}
      ],
      is_activeEp: 0,
      is_activeLang: 0,
    }
  },
  methods: {
    epSelect(id) {
      if (id === this.is_activeEp) {return}
      this.is_activeEp = id
    },
    langSelect(id, title) {
      if (id === this.is_activeLang) {return}
      if (title != "") {
      this.is_activeLang = id
      }
    }
  }
}
</script>

<style lang="scss" scoped>
div, table, th, tr {
  border: 1px solid white;
}

.Guide-ep {
  &-content {
    position: relative;
    display: flex;
  }
  &-table {
    th {
      width: 200px;
    }
  }
  &-subTable {
    width: 100%;
    th {
      width: 200px;
    }
    .Guide-ep-inputBox {
      height: 100px;
    }
  }
}
.tyColor {
  &-success{
    color: $success
  }
  &-danger{
    color: $danger
  }
  &-warning{
    color: $warning
  }
  &-primary{
    color: $primary
  }
}

thead tr th {
  font-size: 22px;
}

tbody tr th input {
  padding-left: var(--space-sm);
  font-size: 22px;
  height: 30px;
  width: 200px;
}

.select {
  &-Ep {
    border-left: 4px solid transparent;
    &-act {
      border-left: 4px solid $primary;
    }
  }
  &-Lang {
    border-bottom: 4px solid transparent;
    &-act {
      border-bottom: 4px solid $primary;
      color: $primary
    }
  }
}

.resTable {
  tr th {
    width: 33%;
  }
}
</style>
