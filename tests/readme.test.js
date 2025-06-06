const fs = require('fs');
const path = require('path');

describe('README Documentation', () => {
  const readmePath = path.resolve(__dirname, '../readme.md');
  let readmeContent;

  beforeAll(() => {
    readmeContent = fs.readFileSync(readmePath, 'utf-8');
  });

  test('README contains Server Integration section', () => {
    expect(readmeContent).toContain('## Server Integration');
  });

  test('Server Integration section has required subsections', () => {
    const requiredSubsections = [
      '### Connection Configuration',
      '### Server Setup',
      '### Connection Examples',
      '### Troubleshooting'
    ];

    requiredSubsections.forEach(subsection => {
      expect(readmeContent).toContain(subsection);
    });
  });

  test('Connection Examples include code snippet', () => {
    expect(readmeContent).toMatch(/```javascript\n\/\/ Example server connection code\nconst serverConnection = {[^}]+}/s);
  });
});