export default class Currency {
  constructor(code, name) {
    this._code = code;
    this._name = name;
  }

  get code() {
    return this._code;
  }

  get name() {
    return this._name;
  }

  set code(newcode) {
    this._code = newcode;
  }

  set name(newname) {
    this._name = newname;
  }

  displayFullCurrency() {
    return `${this.name} (${this.code})`;
  }
}
